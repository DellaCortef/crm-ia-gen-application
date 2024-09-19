import os
import json
import psycopg2
from decimal import Decimal
from dotenv import load_dotenv
from datetime import datetime, time

# Load enviroment variables
load_dotenv()

# Function to connect to PostgreSQL database
def connect_to_postgre():
    conn = psycopg2.connect(
        host=os.environ.get("DB_HOST"),
        database=os.environ.get("DB_NAME"),
        user=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PASS")
    )
    print(conn)
    return conn

# Function to load data from gold_sales_by_product
def load_data_gold_sales_by_product():
    conn = connect_to_postgre()
    query = "SELECT * FROM gold_sales_by_product;"
    with conn.cursor() as cursor:
        cursor.execute(query)
        data = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
    data_dict = [dict(zip(columns, row)) for row in data]
    conn.close
    return data_dict

# Function to load data from load_data_gold_sales_by_seller
def load_data_gold_sales_by_seller():
    conn = connect_to_postgre()
    query = "SELECT * FROM gold_sales_by_seller;"
    with conn.cursor() as cursor:
        cursor.execute(query)
        data = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
    data_dict = [dict(zip(columns, row)) for row in data]
    conn.close
    return data_dict

# Custom serializer for non-serializable types
def custom_serializer(obj):
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    elif isinstance(obj, Decimal):
        return float(obj)
    raise TypeError(f"Type {type(obj)} is not serializable")

# Function to save data into a JSON file
def save_in_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4, default=custom_serializer)

# Main execution: read data and save into JSON files
if __name__ == "__main__":
    sales_data_by_seller = load_data_gold_sales_by_seller()
    save_in_json(sales_data_by_seller, "gold_sales_by_seller.json")

    sales_data_by_product = load_data_gold_sales_by_product()
    save_in_json(sales_data_by_product, "gold_sales_by_product.json")

    print("Data saved in 'gold_vendas_por_vendedor.json' and 'gold_vendas_por_produto.json'.")