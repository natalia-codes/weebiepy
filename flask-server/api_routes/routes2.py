import psycopg2
import os


# hostname = os.environ.get('HOST_NAME')
database = os.environ.get('DB_NAME')
username = os.environ.get('USERNAME')
# password = os.environ.get('DB_PASS')
# port = os.environ.get('PORT')

conn = psycopg2.connect(
    # host = hostname,
    database = database,
    username = username,
    # password = password,
    # port = port
)

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a query
cur.execute("SELECT * FROM data_table")

# Retrieve query results
records = cur.fetchall()

print(records)