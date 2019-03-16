import unittest
import json

from where_is_the_nearest_jump_bike.where_is_the_nearest_jump_bike import where_is_the_nearest_jump_bike


class MyTests(unittest.TestCase):

    def test_where_is_the_nearest_jump_bike(self):
        # e.g.
        # The nearest bike is undocked 20m south south west of here.
        # The nearest is docked at {dock}, 20m east of here.

        # "nearest" or "closest"?

        # 815 E St: 38º35'11" N 121º29'35" W
        # 815 E St: -121.49305556, 38.58638889

        city_park_gps = {
            "longitude": -121.49305556,
            "latitude": 38.58638889
        }

        # hub_4370
        # E St & 9th St
        # -121.4920789003372, 38.586078791838744
        # "905 E Street, Sacramento, CA"

        # https://gps-coordinates.org/distance-between-coordinates.php
        # 110m

        with open('data/free_bike_status.json', 'r') as f:
            free_bike_status = json.load(f)['data']['bikes']

        with open('data/station_status.json', 'r') as f:
            station_status = json.load(f)['data']['stations']

        with open('data/station_information.json', 'r') as f:
            station_information = json.load(f)['data']['stations']

        expected = "The nearest bike is docked at E St & 9th St, 92 m east."
        actual = where_is_the_nearest_jump_bike(free_bike_status, station_status, station_information, city_park_gps)

        self.assertEqual(expected, actual['message'])
