import unittest
from where_is_the_nearest_jump_bike.where_is_the_nearest_jump_bike import direction_between_gps


class DirectionBetweenGpsTests(unittest.TestCase):

    def test_citypark_to_nearest(self):

        from_gps = {
            "longitude": -121.4920789003372,
            "latitude": 38.586078791838744
        }

        to_gps = {
            "longitude": -121.4920789003372,
            "latitude": 38.586078791838744
        }

        expected = "east"

        actual = direction_between_gps(from_gps, to_gps)

        self.assertEqual(expected, actual)

