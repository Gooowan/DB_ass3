import csv
import os
import mysql.connector
from dotenv import load_dotenv
load_dotenv()
def insert_large_sneakers_data(csv_file_path, db_config):
   
    with open(csv_file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        data = []
        for row in csv_reader:
            data.append((row[0], int(row[1]), int(row[2]), float(row[3]), row[4], float(row[5])))

   
    connection = mysql.connector.connect(
        host=db_config['host'],
        user=db_config['user'],
        password=db_config['password'],
        database=db_config['database']
    )
    cursor = connection.cursor()

    insert_query = """
    INSERT INTO Product (name, category_id, remains, rating, description, price)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    cursor.executemany(insert_query, data)
    connection.commit()

    cursor.close()
    connection.close()


"""db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': DB_PASS, # Your pass
    'database': 'SneakerStore'
}"""
db_config = {
    'host': 'localhost',
    'user':  os.getenv("USER"),
    'password':  os.getenv("PASSWORD"),
    'database': os.getenv("DATABASE")
}
#insert_large_sneakers_data('large_sneakers_data.csv', db_config)
#insert_large_user_data('User_500.csv', db_config)
#insert_large_profile_data('Profile_500.csv', db_config)