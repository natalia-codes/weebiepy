import psycopg2
import os
from dotenv import load_dotenv


def get_one_connect():
    load_dotenv()

    hostname = os.getenv('HOST_NAME')
    database = os.getenv('DB_NAME')
    password = os.getenv('DB_PASS')
    port = os.getenv('PORT')

    conn = psycopg2.connect(
        host = hostname,
        database = database,
        password = password,
        port = port
    )

    # Open a cursor to perform database operations
    cur = conn.cursor()

        # Execute a query
    cur.execute("SELECT * FROM data_table WHERE id=1")

    # Retrieve query results
    records = cur.fetchall()

    print(records)

get_one_connect()

 
