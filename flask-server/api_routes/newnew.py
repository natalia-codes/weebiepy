import psycopg2
import os
from dotenv import load_dotenv

class Database: 
    load_dotenv()
    def __init__(self, database, password, port) -> None:
        self.conn = psycopg2.connect(
            
            database = database,
            password = password,
            port = port
        )
    def execute(self, query_string):
        cur = self.conn.cursor()
        cur.execute(query_string)

        return cur.fetchall()

db = Database(os.getenv('DB_NAME'), os.getenv('DB_PASS'), os.getenv('PORT'))

# print(db.execute("SELECT * FROM data_table WHERE id=1"))