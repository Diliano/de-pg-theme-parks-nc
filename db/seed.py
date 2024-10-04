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