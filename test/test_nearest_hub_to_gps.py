import unittest
from where_is_the_nearest_jump_bike.where_is_the_nearest_jump_bike import *


class NearestHubToGpsTests(unittest.TestCase):

    def test_nearest_hub(self):

        gps = {
            "longitude": -121.4920789003372,
            "latitude": 38.586078791838744
        }

        hubs = [
            {"station_id": "hub_4370", "name": "E St & 9th St", "region_id": "region_450", "lon": -121.4920789003372,
             "lat": 38.586078791838744, "address": "905 E Street, Sacramento, CA",
             "rental_methods": ["KEY", "APPLEPAY", "ANDROIDPAY", "TRANSITCARD", "ACCOUNTNUMBER", "PHONE"]},
            {"station_id": "hub_4371", "name": "P St & 21st St", "region_id": "region_450", "lon": -121.48161359131336,
             "lat": 38.56972147552876, "address": "2030 P Street, Sacramento, CA",
             "rental_methods": ["KEY", "APPLEPAY", "ANDROIDPAY", "TRANSITCARD", "ACCOUNTNUMBER", "PHONE"]}
        ]

        expected = hubs[0]

        actual = nearest_station_to_gps(hubs, gps)

        self.assertEqual(expected, actual)

