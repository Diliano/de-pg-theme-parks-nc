from pg8000.native import Connection
from dotenv import load_dotenv
import os

load_dotenv()

user = os.environ["USER"]
db = os.environ["DB"]

# Create your create_conn function to return a database connection object    #

def create_conn():
    return Connection(user=user, database=db)


# Create a close_db function that closes a passed database connection object #

def close_db(conn):
    conn.close()