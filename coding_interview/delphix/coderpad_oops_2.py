import enum

import json
import requests

class FireballError(enum.Enum):
    """
    Enum to store various error messages
    """
    INVALID_COORDINATES = "Latitude and Longitude must be floating point numbers"
    UNREACHABLE_URL = "The API isn't available. Please try again later."
    NULL_OUTPUT = "No shooting star seen since 2017 at the given location"
    INVALID_URL = "Invalid URL. Please check the URL and try again"

class Region():

    def __init__(self, name, *args):

        self.name = name
        self.coordinates = ()
        self.max_brightness = None

    # def adjust_lat_long(self):
    #     pass

    def adjust_lat_long(self, latitude, longitude):
        """
        Returns latitude and longitude range corresponding to a buffer of +/- 15 for visible box.
        Also "normalizes" the range, limiting it to maximum boundary: (-90, 90) for latitude or (-180, 180) for longitude
        :param latitude: (float) latitude for the given location
        :param longitude: (float) longitude for given location
        :return: (tuple) minimum and maximum acceptable values for latitude and longitude comparison
        """
        lat_min = latitude - 15
        lat_min = lat_min if lat_min >= -90 else -90
        lat_max = latitude + 15
        lat_max = lat_max if lat_max <= 90 else 90

        long_min = longitude - 15
        long_min = long_min if long_min >= -180 else -180
        long_max = longitude + 15
        long_max = long_max if long_max <= 180 else 180

        Region.coordinates = (lat_min, lat_max, long_min, long_max)


    def get_max_brightness(self, fireball_data):
        if not self.max_brightness:
            # logic

            return self.max_brightness


class Boston(Region):

    def __init__(self, *args):
        super(Region).__init__(self, *args)


class Fireball:
    def __init__(self):
        """
        For a production scenario, loads brightest location yet from DB - DB be ignored if we don't
        want to persist this value across the invocations

        However, at least, we need to maintain the state (the brightest location), for the current
        session/invocation

        """
        self.brightest_location = {}
        self.fireball_data, self.fireball_fields = None, None

    # underscore - private method
    def get_fireball_data(self, url):
        try:
            output = requests.get(url)
            output.raise_for_status()   #Raises error in case of a Non-200 Response
        except requests.HTTPError:
            return {"Error": FireballError.UNREACHABLE_URL.value}
        except requests.ConnectionError:
            return {"Error": FireballError.INVALID_URL.value}

        data = json.loads(output.text)

        self.fireball_data = data
        self.fireball_fields = data["fields"]

        return data

class BrightestFireball(Fireball):

    def get_contenders(self, coordinates):
        """
        Gets the list of fireball instances whose latitude-longitude falls within the specified coordinate range
        :param coordinates: (list) Latitude-Longitude range
        :param data: (dict) dict containing the details of fireball instances
        :param fields: (list) metadata for fireball instances
        :return: (list) list of fireball instances that fall within specified coordinate range
        """

        contenders = []
        lat_index = self.fireball_fields.index("lat")
        lon_index = self.fireball_fields.index("lon")
        lat_dir_index = self.fireball_fields.index("lat-dir")
        lon_dir_index = self.fireball_fields.index("lon-dir")
        for item in self.fireball_data["data"]:
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


    def get_brightest_fireball(self, location):
        lat_long =next(iter(location.values()))
        try:
            latitude = float(lat_long[0])
            longitude = float(lat_long[1])
        except ValueError:
            return {"Error": FireballError.INVALID_COORDINATES.value}

        coordinates = self.get_lat_long_range(latitude, longitude)
        contenders = self.get_contenders(coordinates)

        if contenders:
            lat_index = self.fireball_fields.index("lat")
            lon_index = self.fireball_fields.index("lon")
            energy_index = self.fireball_fields.index("energy")

            final = max(contenders, key=lambda x: x[energy_index])

            final_dict = {
                "Location" : next(iter(location.keys())),
                "Brightness" : final[energy_index],
                "Coordinates": {
                    "latitude": final[lat_index],
                    "longitude": final[lon_index]
                }

            }

            return final_dict
        return None

    def set_brightest_location(self, location):
        brightest_fireball = self.get_brightest_fireball(location)
        # max_brightness = self.brightest_location["Brightness"]
        if not self.brightest_location:
            self.brightest_location = brightest_fireball
        elif brightest_fireball:
            locations = [self.brightest_location, brightest_fireball]
            # new_brightest_location = max(self.brightest_location, brightest_fireball[1][])
            self.brightest_location = max(locations, key=lambda x: x["Brightness"])


if __name__ == "__main__":
    url = "https://ssd-api.jpl.nasa.gov/fireball.api?date-min=2017-01-01&date-max=2021-01-01"
    fireball = BrightestFireball()
    fireball_data = fireball.get_fireball_data(url)
    # Abstraction - the only interface available to client should be get_brightest_location
    # or the final output
    # client shouldn't worry about calling individual methods of class, e.g. to hit API and
    # populate fireball_data
    # brightest_location.get_fireball_data(url)

    #TODO - Classes for each location
    location_list = [
        {'Boston' : [42.36, -71.05]},
        {'London' : [51.51, -0.12]},
        {'NCR' : [28.58, 77.31]},
        {'San Francisco' : [37.79, -122.40]}

    ]
    # maintain the location list (Location class instance) in the self.brightest_location

    # boston = Boston()

    boston = Region(name="Boston", coordinates=[lat, long])
    london = Region(name="Boston", coordinates=[lat, long])
    ncr = Region(name="Boston", coordinates=[lat, long])
    sf = Region(name="Boston", coordinates=[lat, long])

    region_brightness = {}

    for region in [boston, london, ncr and sf]:
        region_brightness[region.name] = region.get_max_brightness(fireball_data)

    fireball.set_brightest_location(region_brightness)
    #  BrightestFireball ko matlab nhi, usko jo locations doge wo calculate karke de degi

    bf = BrightestFireball()

    adjust latlong and set max_brightness for each location
    boston.adjust_lat_long(42.36, -71.05)
    london.
    ncr
    san_francisco




    boston.get_max_brightness(fireball.get_fireball_data())
    """
    1. Desc order acc. to brightness sort
    2. for each given lat-long range -> which is the first record in the list
    """
    # save date_range and brightest in the location class


    for location in location_list:
        fireball.set_brightest_location(location)

    print(fireball.brightest_location)

"""
Questions
1. Should instance methods return variables or set them in instance variables
2. Should we pass the location_list to calculate it using a function like before 
    or
   Should we maintain a brightest_location as instance variable? and this hulla-hoop of classes
   and instance methods
   
   Depends on whether we wish to maintain state or not.

"""



