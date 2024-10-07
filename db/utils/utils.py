from db.connection import create_conn, close_db
from db.data.index import index as data
from pg8000.native import literal
from copy import deepcopy
# Create your utility functions here, feel free to make additional files


def get_parks_data(column=None):
    db = create_conn()
    if column:
        parks_data = db.run(f"""SELECT * FROM parks ORDER BY {column} DESC;""")
    else:
        parks_data = db.run("""SELECT * FROM parks;""")
    formatted_data = [
        {
            "park_id": park[0],
            "park_name": park[1],
            "year_opened": park[2],
            "annual_attendance": park[3]
        }
        for park in parks_data
    ]
    close_db(db)
    return formatted_data


def get_extended_park_data(id):
    db = create_conn()
    park_data = db.run(f"""SELECT * FROM parks WHERE park_id = {literal(id)}""")[0]
    aggregate_rides_data = db.run(f"""SELECT AVG(votes), COUNT(votes) FROM rides WHERE park_id = {literal(id)}""")[0]
    formatted_data = {
        "park_id": park_data[0],
        "park_name": park_data[1],
        "year_opened": park_data[2],
        "annual_attendance": park_data[3],
        "average_votes": round(float(aggregate_rides_data[0]), 1),
        "ride_count": aggregate_rides_data[1]
    }
    close_db(db)
    return formatted_data


def format_raw_rides_data():
    rides_data = deepcopy(data["rides"])
    parks_data = get_parks_data()

    parks_ids_map = {park["park_name"]: park["park_id"] for park in parks_data}

    for ride in rides_data:
        park_name = ride["park_name"]
        del ride["park_name"]
        ride["park_id"] = parks_ids_map[park_name]

    return rides_data


def get_ride_data(id):
    db = create_conn()
    ride_data = db.run(f"""SELECT * FROM rides WHERE ride_id = {literal(id)}""")[0]
    formatted_data = {
        "ride_id": ride_data[0],
        "park_id": ride_data[1],
        "ride_name": ride_data[2],
        "year_opened": ride_data[3],
        "votes": ride_data[4]
    }
    close_db(db)
    return formatted_data