from db.seed import seed
from db.connection import db
from db.data.index import index as data

# Do not change this code
seed(**data)
db.close()
