import unittest
from where_is_the_nearest_bikeshare_bike.where_is_the_nearest_bikeshare_bike import metres_between_gps


class MetresBetweenGpsTests(unittest.TestCase):

    def test_citypark_to_nearest(self):

        city_park_gps = {
            "longitude": -121.49305556,
            "latitude": 38.58638889
        }

        e_and_ninth_gps = {
            "longitude": -121.4920789003372,
            "latitude": 38.586078791838744
        }

        # http://www.cqsrg.org/tools/GCDistance/
        # 0.091794 km

        # https://www.google.com/maps/dir/'38.58638889,-121.49305556'/'38.586078791838744,-121.4920789003372'/@38.5863537,-121.4931581,18.66z/data=!4m10!4m9!1m3!2m2!1d-121.4930556!2d38.5863889!1m3!2m2!1d-121.4920789!2d38.5860788!3e3
        # 299 ft  ...121m

        expected = 105
        delta = 20

        actual = metres_between_gps(city_park_gps, e_and_ninth_gps)

        self.assertTrue(expected - delta <= actual <= expected + delta)

