

def where_is_the_nearest_jump_bike(free_bike_status, station_information, gps):
    """
    :param free_bike_status: Array of bike
    :param station_information: Array of station_information
    :param gps: Dictionary containing "longitude" and "latitude"
    :return: English sentence directing user to the nearest bike
    """

    # Use Pythagoras to find the closest, determine is it at a hub, calculate distance and direction

    return "unimplemented"


def where_is_the_nearest_hub_with_enough_bikes(station_status, station_information, gps, number_of_bikes):
    """
    :param station_status: Array of station_status
    :param station_information: Array of station_information
    :param gps: Dictionary containing "longitude" and "latitude"
    :param number_of_bikes: required number of Jump bikes
    :return: English sentence directing user to the nearest station with adequate bikes
    """

    # Create lookup dictionary of {station_id: station_information}

    # Iterate through stations status array, if it has >= number_of_bikes, check in station_information is it
    # closer than any recorded previously

    return "unimplemented"


def is_gps_location_a_station(station_information, gps, metres=10):
    """
    :param station_information:
    :param gps:
    :param metres:
    :return: station_information object or False
    """

    # Bikes in free_bike_status.json do not have a property indicating if they are at a hub or not. Let's assume
    # if it's within 10m of a hub, it's at a hub.

    # Use nearest_hub_to_gps then calculate the distance and compare with metres

    return "unimplemented"


def nearest_station_to_gps(station_information, gps):
    """
    :param station_information: Dictionary of {station_id: station_information}
    :param gps: Dictionary containing "longitude" and "latitude"
    :return: station_information object
    """

    # Iterate through stations, use Pythagoras to note closest station.

    return "unimplemented"


def metres_between_gps(from_gps, to_gps):
    """
    :param from_gps: Dictionary containing "longitude" and "latitude"
    :param to_gps: Dictionary containing "longitude" and "latitude"
    :return: Integer distance in metres
    """

    # Copy and paste formula from Stack Overflow:  (a function of latitude)

    return "unimplemented"


def direction_between_gps(from_gps, to_gps):
    """
    :param from_gps: Dictionary containing "longitude" and "latitude"
    :param to_gps: Dictionary containing "longitude" and "latitude"
    :return: String direction, e.g. "north east"
    """

    # Get angle
    # Turn angle to string

    return "unimplemented"


def angle_between_gps(from_gps, to_gps):
    """
    :param from_gps: Dictionary containing "longitude" and "latitude"
    :param to_gps: Dictionary containing "longitude" and "latitude"
    :return: Integer angle using north as 0º
    """

    return "unimplemented"


def angle_to_direction(angle):
    """
    :param angle: Integer angle using north as 0º
    :return: String direction, e.g. "north east"
    """

    # Use switch (assuming Python can use ranges in switches)

    return "unimplemented"

