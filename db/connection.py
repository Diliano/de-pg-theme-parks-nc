import os
from dotenv import load_dotenv
from pg8000.native import Connection

load_dotenv()
PG_USER = os.getenv("PG_USER")
PG_PASSWORD = os.getenv("PG_PASSWORD")
PG_DATABASE = os.getenv("PG_DATABASE")


def get_db():
    '''Returns pg8000 database connection'''
    return Connection(user=PG_USER, password=PG_PASSWORD, database=PG_DATABASE)


db = get_db()

# Create your connection to the DB in this file
