import faker
import os
import mysql.connector
from dotenv import load_dotenv
from mysql.connector import Error

load_dotenv()
fake = faker.Faker()

def insert_to_profile_user(db_config, batch_size=10000):
    try:
        connection = mysql.connector.connect(
            host=db_config['host'],
            user=db_config['user'],
            password=db_config['password'],
            database=db_config['database']
        )
        cursor = connection.cursor()

        profile_insert_query = """
        INSERT INTO Profile (first_name, last_name, shipping_address)
        VALUES (%s, %s, %s)
        """

        user_insert_query = """
        INSERT INTO User (username, password, email, phone, profile_id)
        VALUES (%s, %s, %s, %s, %s)
        """

        print("Inserting profiles in batches...")
        for i in range(0, 500000, batch_size):
            profiles_data = [
                (fake.first_name(), fake.last_name(), fake.address())
                for _ in range(batch_size)
            ]
            cursor.executemany(profile_insert_query, profiles_data)
            connection.commit()

            
            cursor.execute("SELECT id FROM Profile ORDER BY id DESC LIMIT %s", (batch_size,))
            profile_ids = [row[0] for row in cursor.fetchall()]

            print(f"Inserting users for batch {i // batch_size + 1}...")
            users_data = [
                (fake.user_name(), fake.password(), fake.email(), fake.phone_number(), profile_id)
                for profile_id in profile_ids
            ]

            cursor.executemany(user_insert_query, users_data)
            connection.commit()

        cursor.close()
        connection.close()

    except Error as e:
        print(f"Error: {e}")
        if connection.is_connected():
            cursor.close()
            connection.close()


