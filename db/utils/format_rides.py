from db.connection import db


def format_rides(rides):
    '''Formats rides data to insert correct park_id'''
    parks = parks_query_to_dict()
    lookup_park = parks_lookup(parks)

    new_rides = []

    for ride in rides:
        if ride["park_name"] in lookup_park:
            new_rides.append({'park_id': lookup_park.get(ride["park_name"]),
                              'ride_name': ride['ride_name'],
                              'year_opened': ride['year_opened'],
                              'votes': ride['votes']})
    return new_rides


def parks_query_to_dict():
    '''Queries database for inserted parks returns dict'''
    parks = db.run("SELECT * FROM parks;")
    parks_dict = []
    for park in parks:
        park_id, park_name, year_opened, annual_attendance = park
        parks_dict.append({"park_id": park_id,
                           "park_name": park_name,
                           "year_opened": year_opened,
                           "annual_attendance": annual_attendance})
    return parks_dict


def parks_lookup(parks_dict):
    '''Converts parks dict to lookup table'''
    lookup = {}
    for park in parks_dict:
        lookup[park["park_name"]] = park["park_id"]
    return lookup
