import unittest
from where_is_the_nearest_jump_bike.where_is_the_nearest_jump_bike import angle_to_direction


class AngleToDirectionTests(unittest.TestCase):

    def test_north(self):

        angle = 0

        expected = "north"

        actual = angle_to_direction(angle)

        self.assertEqual(expected, actual)

    def test_east(self):

        angle = 90

        expected = "east"

        actual = angle_to_direction(angle)

        self.assertEqual(expected, actual)

    def test_south(self):

        angle = 180

        expected = "south"

        actual = angle_to_direction(angle)

        self.assertEqual(expected, actual)

    def test_west(self):

        angle = 270

        expected = "west"

        actual = angle_to_direction(angle)

        self.assertEqual(expected, actual)

    def test_north_east(self):

        angle = 45

        expected = "north-east"

        actual = angle_to_direction(angle)

        self.assertEqual(expected, actual)

    def test_south_east(self):

        angle = 105

        expected = "south-east"

        actual = angle_to_direction(angle)

        self.assertEqual(expected, actual)

    def test_south_west(self):

        angle = 220

        expected = "south-west"

        actual = angle_to_direction(angle)

        self.assertEqual(expected, actual)

    def test_north_west(self):

        angle = 320

        expected = "north-west"

        actual = angle_to_direction(angle)

        self.assertEqual(expected, actual)
