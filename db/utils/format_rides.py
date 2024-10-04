from db.connection import create_conn, close_db
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
