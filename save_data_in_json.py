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