from pg8000.native import literal
from db.data.index import index as data
from db.utils.format_rides import format_raw_rides_data
# You will need to write your database connection file
# before being able to run your seed file


def seed(db, parks, rides, stalls, foods):
    '''Seeds database'''
    db.run("DROP TABLE IF EXISTS rides;")
    db.run("DROP TABLE IF EXISTS stalls;")
    db.run("DROP TABLE IF EXISTS foods;")
    db.run("DROP TABLE IF EXISTS stalls_foods;")
    db.run("DROP TABLE IF EXISTS parks;")
    create_parks(db)
    create_rides(db)
    insert_parks_data(db)
    insert_rides_data(db)


def create_parks(db):
    '''Create your parks table in the query below'''
    create_query = """
        CREATE TABLE parks (
            park_id SERIAL PRIMARY KEY, 
            park_name VARCHAR(255) NOT NULL, 
            year_opened INTEGER NOT NULL, 
            annual_attendance INTEGER NOT NULL
        );
    """
    return db.run(sql=create_query)


def create_rides(db):
    create_query = """
        CREATE TABLE rides (
            ride_id SERIAL PRIMARY KEY,
            park_id INTEGER REFERENCES parks(park_id),
            ride_name VARCHAR(255) NOT NULL,
            year_opened INTEGER NOT NULL,
            votes INTEGER NOT NULL
        );
    """
    return db.run(sql=create_query)


def insert_parks_data(db):
    parks = data["parks"]
    insert_query = """INSERT INTO parks (park_name, year_opened, annual_attendance) VALUES """
    rows_to_insert = (""", """).join([
        f"""({literal(park["park_name"])}, {literal(park["year_opened"])}, {literal(park["annual_attendance"])})""" for park in parks
    ])
    insert_query += rows_to_insert
    return db.run(sql=insert_query)


def insert_rides_data(db):
    rides = format_raw_rides_data()
    insert_query = """INSERT INTO rides (park_id, ride_name, year_opened, votes) VALUES """
    rows_to_insert = (""", """).join([
        f"""({literal(ride["park_id"])}, {literal(ride["ride_name"])}, {literal(ride["year_opened"])}, {literal(ride["votes"])})""" for ride in rides
    ])
    insert_query += rows_to_insert
    return db.run(sql=insert_query)
