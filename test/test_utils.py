from db.utils.utils import get_parks_data, format_raw_rides_data, get_ride_data
from db.data.index import index as data
from copy import copy
# Write the tests for your utility functions here

class TestGetParksData:
    def test_get_parks_data_returns_formatted_data(self):
        # Arrange
        expected = [
            {
                "park_id": 1,
                "park_name": "Thorpe Park",
                "year_opened": 1979,
                "annual_attendance": 1700000
            },
            {
                "park_id": 2,
                "park_name": "Alton Towers",
                "year_opened": 1980,
                "annual_attendance": 2520000
            },
            {
                "park_id": 3,
                "park_name": "Chessington World of Adventures",
                "year_opened": 1987,
                "annual_attendance": 1400000
            },
            {
                "park_id": 4,
                "park_name": "Tivoli Gardens",
                "year_opened": 1843,
                "annual_attendance": 3972000
            }
        ]
        # Act
        result = get_parks_data()
        # Assert
        assert result == expected


class TestFormatRawRidesData:
    def test_format_raw_rides_data_returns_formatted_data(self):
        # Arrange
        expected = [
            {
                "ride_name": 'Colossus',
                "year_opened": 2002,
                "park_id": 1,
                "votes": 5
            },
            {
                "ride_name": 'Stealth',
                "year_opened": 2006,
                "park_id": 1,
                "votes": 4
            },
            {
                "ride_name": 'Loggers Leap',
                "year_opened": 1989,
                "park_id": 1,
                "votes": 9
            },
            {
                "ride_name": 'Mr Monkeys Banana Ride',
                "year_opened": 1994,
                "park_id": 1,
                "votes": 5
            },
            {
                "ride_name": 'Tidal Wave',
                "year_opened": 2000,
                "park_id": 1,
                "votes": 1
            },
            {
                "ride_name": 'Rocky Express',
                "year_opened": 1989,
                "park_id": 1,
                "votes": 5
            },
            {
                "ride_name": 'Nemesis',
                "year_opened": 1994,
                "park_id": 2,
                "votes": 5
            },
            {
                "ride_name": 'The Smiler',
                "year_opened": 2013,
                "park_id": 2,
                "votes": 1
            },
            {
                "ride_name": 'Rita',
                "year_opened": 2005,
                "park_id": 2,
                "votes": 5
            },
            {
                "ride_name": 'Congo River Rapids',
                "year_opened": 1994,
                "park_id": 2,
                "votes": 3
            },
            {
                "ride_name": 'Enterprise',
                "year_opened": 1984,
                "park_id": 2,
                "votes": 5
            },
            {
                "ride_name": 'Gallopers Carousel',
                "year_opened": 1991,
                "park_id": 2,
                "votes": 7
            },
            {
                "ride_name": 'Rattlesnake',
                "year_opened": 1998,
                "park_id": 3,
                "votes": 11
            },
            {
                "ride_name": 'Tiger Rock',
                "year_opened": 2018,
                "park_id": 3,
                "votes": 3
            },
            {
                "ride_name": 'KOBRA',
                "year_opened": 2010,
                "park_id": 3,
                "votes": 1
            },
            {
                "ride_name": 'Tiny Truckers',
                "year_opened": 1994,
                "park_id": 3,
                "votes": 2
            },
            {
                "ride_name": 'The Demon',
                "year_opened": 2004,
                "park_id": 4,
                "votes": 8
            },
            {
                "ride_name": 'The Caravan',
                "year_opened": 1974,
                "park_id": 4,
                "votes": 1
            },
            {
                "ride_name": 'The Bumper Cars',
                "year_opened": 1926,
                "park_id": 4,
                "votes": 25
            },
            {
                "ride_name": 'The Little Pilot',
                "year_opened": 1990,
                "park_id": 4,
                "votes": 6
            }
        ]
        # Act
        result = format_raw_rides_data()
        # Assert
        assert result == expected

    def test_format_raw_rides_data_leaves_original_data_unchanged(self):
        # Arrange
        rides_data = data["rides"]
        # Act
        result = format_raw_rides_data()
        # Assert
        assert rides_data is not result
        assert data["rides"] is not result


class TestGetRideData:
    def test_get_ride_data_returns_formatted_data(self):
        # Arrange
        test_id = 1
        expected = {
            "ride_id": 1,
            "park_id": 1,
            "ride_name": "Colossus",
            "year_opened": 2002,
            "votes": 5
	    }
        # Act
        result = get_ride_data(test_id)
        # Assert
        assert result == expected

        # Arrange
        test_id = 2
        expected = {
            "ride_id": 2,
            "park_id": 1,
            "ride_name": "Stealth",
            "year_opened": 2006,
            "votes": 4
	    }
        # Act
        result = get_ride_data(test_id)
        # Assert
        assert result == expected