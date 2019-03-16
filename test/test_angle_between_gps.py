import unittest
from where_is_the_nearest_jump_bike.where_is_the_nearest_jump_bike import angle_between_gps


class AngleBetweenGpsTests(unittest.TestCase):

    def test_north_angle(self):
        # Use same GPS except increase latitude

        from_gps = {
            "longitude": -121.49305556,
            "latitude": 38.58638889
        }

        to_gps = {
            "longitude": -121.49305556,
            "latitude": 48.58638889
        }

        expected = 0

        actual = angle_between_gps(from_gps, to_gps)

        self.assertEqual(expected, actual)

    def test_east_angle(self):
        # Use same GPS except increase longitude

        from_gps = {
            "longitude": -121.49305556,
            "latitude": 48.58638889
        }

        to_gps = {
            "longitude": -111.49305556,
            "latitude": 48.58638889
        }

        expected = 90

        actual = angle_between_gps(from_gps, to_gps)

        self.assertEqual(expected, actual)

    def test_south_angle(self):
        # Use same GPS except decrease latitude

        from_gps = {
            "longitude": -121.49305556,
            "latitude": 48.58638889
        }

        to_gps = {
            "longitude": -121.49305556,
            "latitude": 38.58638889
        }

        expected = 180

        actual = angle_between_gps(from_gps, to_gps)

        self.assertEqual(expected, actual)

    def test_west_angle(self):
        # Use same GPS except decrease longitude

        from_gps = {
            "longitude": -121.49305556,
            "latitude": 28.58638889
        }

        to_gps = {
            "longitude": -151.49305556,
            "latitude": 28.58638889
        }

        expected = 0

        actual = angle_between_gps(from_gps, to_gps)

        self.assertEqual(expected, actual)

    def test_angle_between_citypark_and_nearest(self):

        city_park_gps = {
            "longitude": -121.49305556,
            "latitude": 38.58638889
        }

        nearest_hub_gps = {
            "longitude": -121.4920789003372,
            "latitude": 38.586078791838744
        }

        # https://www.calculator.net/slope-calculator.html?type=1&x11=-121.49305556&y11=38.58638889&x12=-121.4920789003372&y12=38.586078791838744&x=36&y=14
        # Compass uses north (y axis) as 0.
        expected = 108

        actual = angle_between_gps(city_park_gps, nearest_hub_gps)

        self.assertEqual(expected, actual)

