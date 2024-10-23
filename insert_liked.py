import faker
import os
import mysql.connector
from dotenv import load_dotenv
from mysql.connector import Error
import random

load_dotenv()
fake = faker.Faker()

def insert_liked_products(db_config, total_entries=5000):
    try:
        connection = mysql.connector.connect(
            host=db_config['host'],
            user=db_config['user'],
            password=db_config['password'],
            database=db_config['database']
        )
        cursor = connection.cursor()

        print("Fetching profile IDs...")
        cursor.execute("SELECT id FROM Profile")
        profile_ids = [row[0] for row in cursor.fetchall()]

        print("Inserting liked products...")
        liked_products_insert_query = """
        INSERT INTO Liked_Products (profile_id, product_id)
        VALUES (%s, %s)
        """

        
        liked_products_data = [
            (random.choice(profile_ids), random.randint(1, 10000))
            for _ in range(total_entries)
        ]

        cursor.executemany(liked_products_insert_query, liked_products_data)
        connection.commit()

        print(f"{total_entries} liked products inserted successfully.")

        cursor.close()
        connection.close()

    except Error as e:
        print(f"Error: {e}")
        if connection.is_connected():
            cursor.close()
            connection.close()



#insert_liked_products(db_config, total_entries=5000)
