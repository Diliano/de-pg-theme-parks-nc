from db.connection import create_conn, close_db
from db.data.index import index as data
from copy import deepcopy
from pprint import pprint
# Create your utility functions here, feel free to make additional files


def get_parks_data():
    db = create_conn()
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


def format_rides_data():
    rides_data = deepcopy(data["rides"])
    parks_data = get_parks_data()

    parks_ids_map = {park["park_name"]: park["park_id"] for park in parks_data}

    for ride in rides_data:
        park_name = ride["park_name"]
        del ride["park_name"]
        ride["park_id"] = parks_ids_map[park_name]

    return rides_data
