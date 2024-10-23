from insert_product import insert_large_sneakers_data
from insert_user_profile import insert_to_profile_user
from insert_liked import insert_liked_products
from insert_order_prodorder import insert_orders_and_order_products
from dotenv import load_dotenv
import os
load_dotenv()

db_config = {
    'host': 'localhost',
    'user':  os.getenv("USER"),
    'password':  os.getenv("PASSWORD"),
    'database': os.getenv("DATABASE")
}
insert_large_sneakers_data('large_sneakers_data.csv', db_config)
insert_to_profile_user(db_config)
insert_liked_products(db_config,total_entries=5000)
insert_orders_and_order_products(db_config)