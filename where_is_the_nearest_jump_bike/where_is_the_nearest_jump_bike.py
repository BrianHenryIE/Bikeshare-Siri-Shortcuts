import math


def where_is_the_nearest_jump_bike(free_bike_status, station_status, station_information, gps):
    """
    :param free_bike_status: Array of bike
    :param station_information: Array of station_information
    :param gps: Dictionary containing "longitude" and "latitude"
    :return: English sentence directing user to the nearest bike
    """

    nearest_bike = {'distance': 999999999}

    # Iterate through, note closest bike.
    for bike in free_bike_status:
        bike_gps = {'longitude': bike['lon'], 'latitude': bike['lat']}
        bike_distance = metres_between_gps(gps, bike_gps)
        athub = is_gps_location_a_station(station_information, bike_gps)
        if bike_distance < nearest_bike['distance']:
            nearest_bike['distance'] = bike_distance
            nearest_bike['undocked'] = bike
            nearest_bike['gps'] = {'longitude': bike['lon'], 'latitude': bike['lat']}

    station_status_dictionary = {station['station_id']: station for station in station_status}

    for station in station_information:
        station_gps = {'longitude': station['lon'], 'latitude': station['lat']}
        station_distance = metres_between_gps(gps, station_gps)
        if station_distance < nearest_bike['distance']:
            single_station_status = station_status_dictionary[station['station_id']]
            if single_station_status['num_bikes_available'] > 0:
                nearest_bike['distance'] = station_distance
                nearest_bike['station'] = station
                nearest_bike['gps'] = {'longitude': station['lon'], 'latitude': station['lat']}
                if 'bike' in nearest_bike.keys():
                    del nearest_bike['bike']

    direction_to_bike = direction_between_gps(gps, nearest_bike['gps'])

    if 'station' in nearest_bike.keys():
        return "The nearest bike is docked at " + nearest_bike['station']['name'] + ", " + str(nearest_bike['distance']) + " m " + direction_to_bike + "."
    else:
        return "The nearest bike is undocked, " + str(nearest_bike['distance']) + " m " + direction_to_bike + "."


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


def is_gps_location_a_station(station_information, gps, metres=15):
    """
    :param station_information:
    :param gps:
    :param metres:
    :return: station_information object or False
    """

    # Bikes in free_bike_status.json do not have a property indicating if they are at a hub or not. Let's assume
    # if it's within 15m of a hub, it's at a hub.

    # Iterate through stations, note closest station.
    for station in station_information:
        station_gps = {'longitude': station['lon'], 'latitude': station['lat']}
        station_distance = metres_between_gps(gps, station_gps)
        if station_distance < metres:
            return station

    return False


def nearest_station_to_gps(station_information, gps):
    """
    :param station_information: Dictionary of {station_id: station_information}
    :param gps: Dictionary containing "longitude" and "latitude"
    :return: station_information object
    """

    nearest_station = station_information[0]
    nearest_distance = 9999999

    # Iterate through stations, use Pythagoras to note closest station.
    for station in station_information:
        station_gps = {'longitude': station['lon'], 'latitude': station['lat']}
        station_distance = metres_between_gps(gps, station_gps)
        if station_distance < nearest_distance:
            nearest_distance = station_distance
            nearest_station = station

    return nearest_station


def metres_between_gps(from_gps, to_gps):
    """
    :param from_gps: Dictionary containing "longitude" and "latitude"
    :param to_gps: Dictionary containing "longitude" and "latitude"
    :return: Integer distance in metres
    """

    # https://stackoverflow.com/a/19412565/336146

    R = 6373.0

    lat1 = math.radians(from_gps['latitude'])
    lon1 = math.radians(from_gps['longitude'])
    lat2 = math.radians(to_gps['latitude'])
    lon2 = math.radians(to_gps['longitude'])

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distance = R * c * 1000

    return round(distance)


def direction_between_gps(from_gps, to_gps):
    """
    :param from_gps: Dictionary containing "longitude" and "latitude"
    :param to_gps: Dictionary containing "longitude" and "latitude"
    :return: String direction, e.g. "north east"
    """

    angle = angle_between_gps(from_gps, to_gps)

    direction = angle_to_direction(angle)

    return direction


def angle_between_gps(from_gps, to_gps):
    """
    :param from_gps: Dictionary containing "longitude" and "latitude"
    :param to_gps: Dictionary containing "longitude" and "latitude"
    :return: Integer angle using north as 0º
    """

    # Move to_gps as though from_gps is 0,0
    centered_gps = {
        'longitude': to_gps['longitude'] - from_gps['longitude'],
        'latitude': to_gps['latitude'] - from_gps['latitude']
    }

    if centered_gps['latitude'] == 0:
        # either 90 or 270
        if to_gps['longitude'] > from_gps['longitude']:
            return 90
        else:
            return 270

    if centered_gps['longitude'] == 0:
        # either 90 or 270
        if to_gps['latitude'] > from_gps['latitude']:
            return 0
        else:
            return 180

    angle = math.degrees(math.atan2(centered_gps['latitude'], centered_gps['longitude']))

    # clockwise from horizontal
    if 0 >= angle >= -90:
        compass_angle = math.fabs(angle) + 90

    if -90 >= angle >= -180:
        compass_angle = math.fabs(angle) + 90

    # anti-clockwise from horizontal
    if 0 <= angle < 90:
        compass_angle = 90 - angle

    if 90 <= angle < 180:
        compass_angle = 360 - (angle - 90)

    return round(compass_angle)


def angle_to_direction(angle):
    """
    :param angle: Integer angle using north as 0º
    :return: String direction, e.g. "north-east"
    """

    if 0 <= angle < 23: return 'north'
    if 23 <= angle < 68: return 'north-east'
    if 68 <= angle < 113: return 'east'
    if 113 <= angle < 158: return 'south-east'
    if 158 <= angle < 203: return 'south'
    if 203 <= angle < 248: return 'south-west'
    if 248 <= angle < 293: return 'west'
    if 293 <= angle < 337: return 'north-west'
    if 337 <= angle < 360: return 'north'

    return None

