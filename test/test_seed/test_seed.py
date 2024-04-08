import pytest
from db.seed import seed
from db.connection import db
from db.data.index import index as data

# Do not change these tests


@pytest.fixture(scope="session")
def run_seed():
    '''Runs seed before starting tests, yields, runs tests,
       then closes connection to db'''
    seed(**data)
    yield
    db.close()


# Parks table tests
def test_parks_table_exists(run_seed):
    '''Tests if parks table exists'''
    base_query = "SELECT EXISTS (SELECT FROM information_schema.tables \
                  WHERE table_name = 'parks')"
    expect = db.run(base_query)
    assert expect == [[True]]


def test_parks_table_has_park_id_column_as_serial_primary_key(run_seed):
    '''Tests if parks table has park_id as serial primary key'''
    base_query = "SELECT column_name, data_type, column_default \
                  FROM information_schema.columns \
                  WHERE table_name = 'parks' \
                  AND column_name = 'park_id';"
    expect = db.run(base_query)
    assert expect[0][0] == "park_id"
    assert expect[0][1] == "integer"
    assert expect[0][2] == "nextval('parks_park_id_seq'::regclass)"


def test_parks_table_has_park_name_column(run_seed):
    '''Tests if parks table has park name column'''
    base_query = "SELECT column_name, data_type, column_default \
                  FROM information_schema.columns \
                  WHERE table_name = 'parks' \
                  AND column_name = 'park_name';"
    expect = db.run(base_query)
    assert expect == [["park_name", "character varying", None]]


def test_parks_table_has_park_id_column(run_seed):
    '''Tests if parks table has park id column'''
    base_query = "SELECT column_name \
                  FROM information_schema.columns \
                  WHERE table_name = 'parks' \
                  AND column_name = 'park_id';"
    expect = db.run(base_query)
    assert expect == [["park_id"]]


def test_parks_table_has_year_opened_column(run_seed):
    '''Tests if parks table has year opened column'''
    base_query = "SELECT column_name \
                  FROM information_schema.columns \
                  WHERE table_name = 'parks' \
                  AND column_name = 'year_opened';"
    expect = db.run(base_query)
    assert expect == [["year_opened"]]


def test_parks_table_has_annual_attendance_column(run_seed):
    '''Tests if parks table has annual attendance column'''
    base_query = "SELECT column_name \
                  FROM information_schema.columns \
                  WHERE table_name = 'parks' \
                  AND column_name = 'annual_attendance';"
    expect = db.run(base_query)
    assert expect == [["annual_attendance"]]


# Rides table tests
def test_rides_table_exists(run_seed):
    '''Tests if rides table exists'''
    base_query = "SELECT EXISTS (SELECT FROM information_schema.tables \
                  WHERE table_name = 'rides');"
    expect = db.run(base_query)
    assert expect == [[True]]


def test_rides_table_has_ride_id_column_as_serial_primary_key(run_seed):
    '''Tests if rides table has ride id as serial primary key'''
    base_query = "SELECT column_name, data_type, column_default \
                  FROM information_schema.columns \
                  WHERE table_name = 'rides' \
                  AND column_name = 'ride_id';"
    expect = db.run(base_query)
    assert expect[0][0] == "ride_id"
    assert expect[0][1] == "integer"
    assert expect[0][2] == "nextval('rides_ride_id_seq'::regclass)"


def test_rides_table_has_ride_name_column(run_seed):
    '''Tests if rides table has ride name column'''
    base_query = "SELECT column_name, data_type, column_default \
                  FROM information_schema.columns \
                  WHERE table_name = 'rides' \
                  AND column_name = 'ride_name';"
    expect = db.run(base_query)
    assert expect == [["ride_name", "character varying", None]]


def test_rides_table_has_ride_id_column(run_seed):
    '''Tests if rides table has ride id column'''
    base_query = "SELECT column_name \
                  FROM information_schema.columns \
                  WHERE table_name = 'rides' \
                  AND column_name = 'ride_id';"
    expect = db.run(base_query)
    assert expect == [["ride_id"]]


def test_rides_table_has_year_opened_column(run_seed):
    '''Tests if rides table has year opened column'''
    base_query = "SELECT column_name \
                  FROM information_schema.columns \
                  WHERE table_name = 'rides' \
                  AND column_name = 'year_opened';"
    expect = db.run(base_query)
    assert expect == [["year_opened"]]


def test_rides_table_has_votes_column(run_seed):
    '''Tests if rides table has votes column'''
    base_query = "SELECT column_name \
                  FROM information_schema.columns \
                  WHERE table_name = 'rides' \
                  AND column_name = 'votes';"
    expect = db.run(base_query)
    assert expect == [["votes"]]


# Data insertion
def test_parks_data_has_been_inserted_correctly(run_seed):
    '''Tests if parks data has been inserted correctly'''
    base_query = "SELECT * FROM parks;"
    parks = db.run(base_query)

    assert len(parks) == 4

    for park in parks:
        park_id, park_name, year_opened, annual_attendance = park
        assert isinstance(park_id, int)
        assert isinstance(park_name, str)
        assert isinstance(year_opened, int)
        assert isinstance(annual_attendance, int)


def test_rides_data_has_been_inserted_correctly(run_seed):
    '''Tests if rides data has been inserted correctly'''
    base_query = "SELECT * FROM rides;"
    rides = db.run(base_query)

    assert len(rides) == 20

    for ride in rides:
        ride_id, park_id, ride_name, year_opened, votes = ride
        assert isinstance(ride_id, int)
        assert isinstance(park_id, int)
        assert isinstance(ride_name, str)
        assert isinstance(year_opened, int)
        assert isinstance(votes, int)
