from db.connection import db
from db.utils.format_rides import format_rides


def seed(parks, rides, stalls, foods):
    '''Seeds database'''
    db.run("DROP TABLE IF EXISTS rides;")
    db.run("DROP TABLE IF EXISTS stalls;")
    db.run("DROP TABLE IF EXISTS foods;")
    db.run("DROP TABLE IF EXISTS stalls_foods;")
    db.run("DROP TABLE IF EXISTS parks;")
    create_parks()
    create_rides()
    insert_parks(parks)
    formatted_rides = format_rides(rides)
    insert_rides(formatted_rides)


def create_parks():
    '''Create your parks table in the query below'''
    return db.run("CREATE TABLE parks ( \
                  park_id SERIAL PRIMARY KEY, \
                  park_name VARCHAR NOT NULL, \
                  year_opened INT NOT NULL, \
                  annual_attendance INT NOT NULL);")


def create_rides():
    '''Create rides table'''
    return db.run("CREATE TABLE rides ( \
                  ride_id SERIAL PRIMARY KEY, \
                  park_id INT REFERENCES parks(park_id), \
                  ride_name VARCHAR NOT NULL, \
                  year_opened INT NOT NULL, \
                  votes INT NOT NULL)")


def insert_parks(parks):
    '''Inserts parks data into parks table'''
    for park in parks:
        params = {'park_name': park["park_name"],
                  'year_opened': park["year_opened"],
                  'annual_attendance': park["annual_attendance"]}
        base_query = "INSERT INTO parks (park_name, \
                                         year_opened, \
                                         annual_attendance) \
                                VALUES (:park_name, \
                                        :year_opened, \
                                        :annual_attendance);"
        db.run(base_query, **params)


def insert_rides(formatted_rides):
    '''Inserts formatted rides data into rides table'''
    for ride in formatted_rides:
        params = {'park_id': ride["park_id"],
                  'ride_name': ride["ride_name"],
                  'year_opened': ride["year_opened"],
                  'votes': ride["votes"]}
        base_query = "INSERT INTO rides (park_id, \
                                         ride_name, \
                                         year_opened, \
                                         votes) \
                                 VALUES (:park_id, \
                                         :ride_name, \
                                         :year_opened, \
                                         :votes);"
        db.run(base_query, **params)
