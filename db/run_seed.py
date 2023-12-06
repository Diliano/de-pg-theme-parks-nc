from db.seed import seed
from db.connection import db
from db.data.index import index as data

# Do not change this code
try:
    seed(**data)
except Exception as e:
    print(e)
finally:
    db.close()
