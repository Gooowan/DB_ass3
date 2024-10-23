import faker
import os
import mysql.connector
from dotenv import load_dotenv
from mysql.connector import Error
import random
from datetime import datetime

load_dotenv()
fake = faker.Faker()

def insert_orders_and_order_products(db_config, num_orders=500000, batch_size=15000):
    try:
        connection = mysql.connector.connect(
            host=db_config['host'],
            user=db_config['user'],
            password=db_config['password'],
            database=db_config['database']
        )
        cursor = connection.cursor()

      
        print("Truncating Order_Product and Order tables...")
        cursor.execute("SET FOREIGN_KEY_CHECKS = 0")  
        cursor.execute("TRUNCATE TABLE Order_Product")
        cursor.execute("TRUNCATE TABLE `Order`")
        cursor.execute("SET FOREIGN_KEY_CHECKS = 1") 
        connection.commit()
        print("Tables truncated successfully.")

        print("Fetching profile IDs...")
        cursor.execute("SELECT id FROM Profile")
        profile_ids = [row[0] for row in cursor.fetchall()]

        order_insert_query = """
        INSERT INTO `Order` (profile_id, total_cost, created, paid)
        VALUES (%s, %s, %s, %s)
        """

        order_product_insert_query = """
        INSERT INTO Order_Product (order_id, product_id, quantity)
        VALUES (%s, %s, %s)
        """

        print("Inserting orders in batches...")
        total_inserted_orders = 0

        for i in range(0, num_orders, batch_size):
            print(f"Inserting batch {i // batch_size + 1} of orders...")
            
            orders_data = [
                (
                    random.choice(profile_ids), 
                    round(random.uniform(10.00, 1000.00), 2), 
                    fake.date_this_decade(), 
                    fake.boolean()  
                )
                for _ in range(batch_size)
            ]
            cursor.executemany(order_insert_query, orders_data)
            connection.commit()


            cursor.execute("SELECT id FROM `Order` ORDER BY id DESC LIMIT %s", (batch_size,))
            order_ids = [row[0] for row in cursor.fetchall()]

        
            order_products_data = []
            for order_id in order_ids:
                num_products_in_order = random.randint(1, 5) 
                product_ids = set() 

                while len(product_ids) < num_products_in_order:
                    product_id = random.randint(1, 10000) 
                    if product_id not in product_ids: 
                        product_ids.add(product_id)
                        quantity = random.randint(1, 10)
                        order_products_data.append((order_id, product_id, quantity))

          
            cursor.executemany(order_product_insert_query, order_products_data)
            connection.commit()

            total_inserted_orders += batch_size
            print(f"Total orders inserted: {total_inserted_orders}")

        cursor.close()
        connection.close()
        print(f"Successfully inserted {num_orders} orders and corresponding products.")

    except Error as e:
        print(f"Error: {e}")
        if connection.is_connected():
            cursor.close()
            connection.close()



#insert_orders_and_order_products(db_config, num_orders=500000, batch_size=10000)
