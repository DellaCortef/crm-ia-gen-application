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

