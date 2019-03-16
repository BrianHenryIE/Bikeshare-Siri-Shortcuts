import unittest
from where_is_the_nearest_bikeshare_bike.where_is_the_nearest_bikeshare_bike import nearest_station_to_gps


class NearestStationToGpsTests(unittest.TestCase):

    def test_nearest_station(self):

        # 10 m difference according to Google:
        # https://www.google.com/maps/dir/'38.5863,-121.4930'/'38.58625,-121.4929'/@38.5863537,-121.4931581,18z/data=!4m10!4m9!1m3!2m2!1d-121.493!2d38.5863!1m3!2m2!1d-121.4929!2d38.58625!3e3

        # https://www.wolframalpha.com/input/?i=distance+between+(38.5863,-121.4930),(38.58625,-121.4929)
        # (38.5863,-121.4930),(38.58625,-121.4929)
        # 0.000111

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

