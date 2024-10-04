from db.utils.format_rides import get_parks_data
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