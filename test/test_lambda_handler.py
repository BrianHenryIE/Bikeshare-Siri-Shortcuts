import unittest
from where_is_the_nearest_bikeshare_bike.where_is_the_nearest_bikeshare_bike import lambda_handler

# TODO Error fetching bikeshare data


class LambdaHandlerTests(unittest.TestCase):

    def test_lambda(self):

        # https://rydjo4kddd.execute-api.us-west-2.amazonaws.com/default/?longitude=-121.49305556&latitude=38.58638889

        city_park_gps = {
            "longitude": "-121.49305556",
            "latitude": "38.58638889"
        }

        event = {"queryStringParameters": {
            "latitude": city_park_gps['latitude'],
            "longitude": city_park_gps['longitude']
        }}

        expected = 0

        actual = lambda_handler(event, None)

        print(actual)

        self.assertTrue(actual['body']['distance'] > 0, 'test_lambda')
        # self.assertEqual(expected, actual, 'test_lambda')#


