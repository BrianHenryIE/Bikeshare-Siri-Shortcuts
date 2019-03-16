import unittest
from where_is_the_nearest_jump_bike.where_is_the_nearest_jump_bike import metres_between_gps


class MetresBetweenGpsTests(unittest.TestCase):

    def test_citypark_to_nearest(self):

        from_gps = {
            "longitude": -121.4920789003372,
            "latitude": 38.586078791838744
        }

        to_gps = {
            "longitude": -121.4920789003372,
            "latitude": 38.586078791838744
        }

        expected = 110

        actual = metres_between_gps(from_gps, to_gps)

        self.assertEqual(expected, actual)

