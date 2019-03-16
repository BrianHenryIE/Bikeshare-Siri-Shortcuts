import unittest
from where_is_the_nearest_bikeshare_bike.where_is_the_nearest_bikeshare_bike import direction_between_gps


class DirectionBetweenGpsTests(unittest.TestCase):

    def test_citypark_to_nearest(self):

        city_park_gps = {
            "longitude": -121.49305556,
            "latitude": 38.58638889
        }

        e_and_ninth_gps = {
            "longitude": -121.4920789003372,
            "latitude": 38.586078791838744
        }

        expected = "east"

        actual = direction_between_gps(city_park_gps, e_and_ninth_gps)

        self.assertEqual(expected, actual)

