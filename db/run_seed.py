from db.seed import seed
from db.connection import create_conn, close_db
from db.data.index import index as data

# Do not change this code
try:
    db = create_conn()
    seed(db, **data)
except Exception as e:
    print(e)
finally:
    close_db(db)
