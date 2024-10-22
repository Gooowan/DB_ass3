import csv
import mysql.connector

def insert_large_sneakers_data(csv_file_path, db_config):
    # Step 1: Read the CSV file
    with open(csv_file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        data = []
        for row in csv_reader:
            data.append((row[0], int(row[1]), int(row[2]), float(row[3]), row[4], float(row[5])))

    # Step 3: Connect to the database
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

# Example usage
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': DB_PASS, # Your pass
    'database': 'SneakerStore'
}
insert_large_sneakers_data('large_sneakers_data.csv', db_config)