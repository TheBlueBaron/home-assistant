import os
import googlemaps
import random

class Maps:

    # Allowed categories is based on the allowed place types that can be found here
    # https://developers.google.com/maps/documentation/places/web-service/supported_types#table1

    allowed_categories = [
        "accounting",
        "airport",
        "amusement park",
        "aquarium",
        "art gallery",
        "atm",
        "bakery",
        "bank",
        "bar",
        "beauty salon",
        "bicycle store",
        "book store",
        "bowling alley",
        "bus station",
        "cafe",
        "campground",
        "car dealer",
        "car rental",
        "car repair",
        "car wash",
        "casino",
        "cemetery",
        "church",
        "city hall",
        "clothing store",
        "convenience store",
        "courthouse",
        "dentist",
        "department store",
        "doctor",
        "drugstore",
        "electrician",
        "electronics store",
        "embassy",
        "fire station",
        "florist",
        "funeral home",
        "furniture store",
        "gas station",
        "gym",
        "hair care",
        "hardware store",
        "hindu temple",
        "home goods store",
        "hospital",
        "insurance agency",
        "jewelry store",
        "laundry",
        "lawyer",
        "library",
        "light rail station",
        "liquor store",
        "local government office",
        "locksmith",
        "lodging",
        "meal delivery",
        "meal takeaway",
        "mosque",
        "movie rental",
        "movie theater",
        "moving company",
        "museum",
        "night club",
        "painter",
        "park",
        "parking",
        "pet store",
        "pharmacy",
        "physiotherapist",
        "plumber",
        "police",
        "post office",
        "primary school",
        "real estate agency",
        "restaurant",
        "roofing contractor",
        "rv park",
        "school",
        "secondary school",
        "shoe store",
        "shopping mall",
        "spa",
        "stadium",
        "storage",
        "store",
        "subway station",
        "supermarket",
        "synagogue",
        "taxi stand",
        "tourist attraction",
        "train station",
        "transit station",
        "travel agency",
        "university",
        "veterinary care",
        "zoo",
    ]

    def __init__(self):
        self.google_maps = googlemaps.Client(key=os.getenv('GOOGLE_MAPS_API_KEY'))

    def search_nearby(self, location, category):

        location_geocode = self.google_maps.geocode(location)

        location_lat_lng = (location_geocode[0]['geometry']['location']['lat'], location_geocode[0]['geometry']['location']['lng'])

        nearby_locations = self.google_maps.places_nearby(location=location_lat_lng, radius=1000, type=category)

        formatted_locations = []

        for i in range(len(nearby_locations['results'])):
            found_location = {'Name' : nearby_locations['results'][i]['name'], 'Address' : nearby_locations['results'][i]['vicinity']}
            formatted_locations.append(found_location)

        return formatted_locations

    def random_location_choice(self, location, category):

        locations = self.search_nearby(location, category)

        random_index = random.randint(0, (len(locations)) - 1)

        return locations[random_index]

        