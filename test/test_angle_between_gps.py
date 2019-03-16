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

        self.assertEqual(expected, actual, 'test_north_angle')

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

        self.assertEqual(expected, actual, 'test_east_angle')

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

        self.assertEqual(expected, actual, 'test_south_angle')

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

        expected = 270

        actual = angle_between_gps(from_gps, to_gps)

        self.assertEqual(expected, actual, 'test_west_angle')

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

        self.assertEqual(expected, actual, 'test_angle_between_citypark_and_nearest hub')


    def test_north_east(self):

        city_park_gps = {
            "longitude": -121.49305556,
            "latitude": 38.58638889
        }

        chipotle_in_arden = {
            "longitude": -121.417894,
            "latitude": 38.59719
        }

        # https://www.wolframalpha.com/input/?i=graph+(-121.49305556,+38.58638889)+(-121.417894,+38.59719)

        expected = 82

        actual = angle_between_gps(city_park_gps, chipotle_in_arden)

        self.assertEqual(expected, actual, 'test_north_east city park to arden')

    def test_north_west(self):

        city_park_gps = {
            "longitude": -121.49305556,
            "latitude": 38.58638889
        }

        jimboom_street_bridge = {
            "longitude": -121.5070186,
            "latitude": 38.5997365
        }

        # https://www.wolframalpha.com/input/?i=graph+(-121.49305556,+38.58638889)+(-121.5070186,+38.5997365)

        # https://www.calculator.net/slope-calculator.html?type=1&x11=-121.49305556&y11=38.58638889&x12=-121.5070186&y12=38.5997365&x=58&y=21
        # 136
        # Compass uses north (y axis) as 0.
        expected = 314

        actual = angle_between_gps(city_park_gps, jimboom_street_bridge)

        self.assertEqual(expected, actual, 'test_north_west city park to jimboom street bridge')

    def test_south_west(self):

        city_park_gps = {
            "longitude": -121.49305556,
            "latitude": 38.58638889
        }

        amtrak_station = {
            "longitude": -121.5016916,
            "latitude": 38.5840008,
        }

        # https://www.wolframalpha.com/input/?i=graph+(-121.49305556,+38.58638889)+(-121.5016916,+38.5840008)

        # https://www.calculator.net/slope-calculator.html?type=1&x11=-121.49305556&y11=38.58638889&x12=-121.5070186&y12=38.5997365&x=58&y=21
        # 195
        # Compass uses north (y axis) as 0.
        expected = 255

        actual = angle_between_gps(city_park_gps, amtrak_station)

        self.assertEqual(expected, actual, 'test_south_west city park to amtrak')

    def test_south_east(self):

        city_park_gps = {
            "longitude": -121.49305556,
            "latitude": 38.58638889
        }

        sacramento_bicycle_kitchen = {
            "longitude": -121.4821897,
            "latitude": 38.5783092
        }

        # https://www.wolframalpha.com/input/?i=graph+(-121.49305556,+38.58638889)+(-121.4821897,+38.5783092)

        expected = 127

        actual = angle_between_gps(city_park_gps, sacramento_bicycle_kitchen)

        self.assertEqual(expected, actual, 'test_south_east citypark to bike kitchen')

