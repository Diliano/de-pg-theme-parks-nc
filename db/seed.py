from db.connection import db
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


def create_parks(db):
    '''Create your parks table in the query below'''
    return db.run("")
