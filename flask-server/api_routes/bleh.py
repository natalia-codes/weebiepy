# from api_routes import Database
from newnew import *



# db = Database(os.getenv('DB_NAME'), os.getenv('DB_PASS'), os.getenv('PORT'))
print(db.execute("SELECT * FROM data_table WHERE id=1"))