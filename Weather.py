import requests
from dotenv import load_dotenv
import os
import json

class Weather:

    def get_weather_forecast(self):

        return 0

    def get_weather_locations(self):

        query = f"http://datapoint.metoffice.gov.uk/public/data/val/wxfcs/all/json/sitelist?key={os.getenv('DATAPOINT_API_KEY')}"

        response = requests.get(query)

        response_json = response.json()

        json_object = json.dumps(response_json)

        json_load = json.loads(json_object)

        return json_load

    def get_site_id(self, weather_locations, location):

        id = ""

        for dict in weather_locations["Locations"]["Location"]:
            if dict["name"] == location:
                id = dict["id"]
                break

        return id

    def get_forecast(self, site_id):

        query = f"http://datapoint.metoffice.gov.uk/public/data/val/wxfcs/all/json/{site_id}?res=3hourly&key={os.getenv('DATAPOINT_API_KEY')}"

        response = requests.get(query)

        response_json = response.json()

        json_object = json.dumps(response_json)

        json_load = json.loads(json_object)

        # print(json_object)

        return json_load


