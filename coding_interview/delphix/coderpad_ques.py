import enum
import json
import unittest

import requests


class FireballError(enum.Enum):
    """
    Enum to store various error messages
    """
    INVALID_COORDINATES = "Latitude and Longitude must be floating point numbers"
    UNREACHABLE_URL = "The API isn't available. Please try again later."
    NULL_OUTPUT = "No shooting star seen since 2017 at the given location"
    INVALID_URL = "Invalid URL. Please check the URL and try again"

def get_lat_long_range(latitude: float, longitude):
    """
    Returns latitude and longitude range corresponding to a buffer of +/- 15 for visible box.
    Also "normalizes" the range, limiting it to maximum boundary: (-90, 90) for latitude or (-180, 180) for longitude
    :param latitude: (float) latitude for the given location
    :param longitude: (float) longitude for given location
    :r eturn: (tuple) minimum and maximum acceptable values for latitude and longitude comparison
    """
    lat_min = latitude - 15
    lat_min = lat_min if lat_min >= -90 else -90
    lat_max = latitude + 15
    lat_max = lat_max if lat_max <= 90 else 90

    long_min = longitude - 15
    long_min = long_min if long_min >= -180 else -180
    long_max = longitude + 15
    long_max = long_max if long_max <= 180 else 180

    return (lat_min, lat_max, long_min, long_max)


def fireball(latitude, longitude):
    """
    Makes a GET request to the NASA Fireball Data API (https://ssd-api.jpl.nasa.gov/doc/fireball.html) for list of
    fireballs since 2017 and out of the entries within the calculated range for given latitude and longitude, returns
    data for the entry with the maximum brightness (energy).

    Returns None in case no such entry is found
    :param latitude: (float) latitude for the given location
    :param longitude:  (float) longitude for given location
    :return: (dict) Brightness and Location coordinates
    """

    try:
        latitude = float(latitude)
        longitude = float(longitude)
    except (ValueError, TypeError):
        return {"Error": FireballError.INVALID_COORDINATES.value}

    url = "https://ssd-api.jpl.nasa.gov/fireball.api?date-min=2017-01-01&date-max=2021-01-01"

    try:
        output = requests.get(url)
        output.raise_for_status()   #Raises error in case of a Non-200 Response
    except requests.HTTPError:
        return {"Error": FireballError.UNREACHABLE_URL.value}
    except requests.ConnectionError:
        return {"Error": FireballError.INVALID_URL.value}

    coordinates = get_lat_long_range(latitude, longitude)


    data = json.loads(output.text)

    fields = data["fields"]

    contenders = get_contenders(coordinates, data, fields)

    if contenders:
        lat_index = fields.index("lat")
        lon_index = fields.index("lon")
        energy_index = fields.index("energy")

        final = max(contenders, key=lambda x: x[energy_index])

        final_dict = {
            "Brightness" : final[energy_index],
            "Location": {
                "latitude": final[lat_index],
                "longitude": final[lon_index]
            }

        }

        return final_dict
    return None


def get_contenders(coordinates, data, fields):
    """
    Gets the list of fireball instances whose latitude-longitude falls within the specified coordinate range
    :param coordinates: (list) Latitude-Longitude range
    :param data: (dict) dict containing the details of fireball instances
    :param fields: (list) metadata for fireball instances
    :return: (list) list of fireball instances that fall within specified coordinate range
    """
    contenders = []
    lat_index = fields.index("lat")
    lon_index = fields.index("lon")
    lat_dir_index = fields.index("lat-dir")
    lon_dir_index = fields.index("lon-dir")
    for item in data["data"]:
        lat_dir, lon_dir = item[lat_dir_index], item[lon_dir_index]
        if lat_dir:
            # Conversion to Signed Degrees
            lat, lon = item[lat_index], item[lon_index]
            if lat_dir == 'S':
                lat = -1 * float(lat)
            else:
                lat = float(lat)
            if item[6] == 'W':
                lon = -1 * float(lon)
            else:
                lon = float(lon)

            if lat >= coordinates[0] and lat <= coordinates[1] and lon >= coordinates[2] and lon <= coordinates[3]:
                contenders.append(item)
    return contenders


def determine_location_max_brightness():
    """
    :return: (str) string containing the city name among "Boston", "London", "NCR" and "San Francisco" which saw the fireball
    maximum energy
    """

    delphix_boston = [42.36, -71.05]
    delphix_london = [51.51, -0.12]
    delphix_ncr = [28.58, 77.31]
    delphix_sf = [37.79, -122.40]

    brightest_boston = ["Boston", fireball(delphix_boston[0], delphix_boston[1])]
    brightest_london = ["London", fireball(delphix_london[0], delphix_london[1])]
    brightest_ncr = ["NCR", fireball(delphix_ncr[0], delphix_ncr[1])]
    brightest_sf = ["San Francisco", fireball(delphix_sf[0], delphix_sf[1])]x

    city_list = list(filter(None, [brightest_boston, brightest_london, brightest_ncr, brightest_sf]))

    if city_list:

        location_max_brightness = max(city_list, key=lambda x: x[1]["Brightness"])

        result = f"Location with maximum bri    ghtness: {location_max_brightness[0]}"

        return result


class TestFireball(unittest.TestCase):

    # set

    def test_passed_coordinates(self):
        expected = {"Error": FireballError.INVALID_COORDINATES.value}
        actual = fireball('latitude', 'longitude')
        self.assertEqual(expected, actual)

    def test_coordinate_range_normalization(self):
        latitude = 85
        longitude = -175
        coordinates = get_lat_long_range(latitude, longitude)

        self.assertGreaterEqual(coordinates[0], -90)
        self.assertLessEqual(coordinates[1], 90)
        self.assertGreaterEqual(coordinates[2], -180)
        self.assertLessEqual(coordinates[3], 180)

    def test_output_success(self):
        latitude = '28.58'
        longitude = '77.31'

        expected = {'Brightness': '2.7', 'Location': {'latitude': '28.2', 'longitude': '76.7'}}
        actual = fireball(latitude, longitude)

        self.assertEqual(expected, actual)

    def test_location_with_max_brightness(self):
       expected = f"Location with maximum brightness: Boston"
       actual = determine_location_max_brightness()

       self.assertEqual(expected, actual)

if __name__ == "__main__":

    print(determine_location_max_brightness())
    # unittest.main()


"""

1. Abstraction
2. Modularisation
3. Exception Handling
4. Reusability
5. Basic coding standards
6. Production readiness


"""