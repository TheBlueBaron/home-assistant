import requests
from dotenv import load_dotenv
import os
import json
import datetime

class Weather:

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

        current_day_forecasts = json_load["SiteRep"]["DV"]["Location"]["Period"][0]["Rep"]

        current_time = datetime.datetime.now()
        current_hour = current_time.hour

        forecast_band = int(0)

        match current_hour:
            case 0 | 1 | 2:
                forecast_band = int(0)
            case 3 | 4 | 5:
                forecast_band = int(180)
            case 6 | 7 | 8:
                forecast_band = int(360)
            case 9 | 10 | 11:
                forecast_band = int(540)
            case 12 | 13 | 14:
                forecast_band = int(720)
            case 15 | 16 | 17:
                forecast_band = int(900)
            case 18 | 19 | 20:
                forecast_band = int(1080)
            case 21 | 22 | 23:
                forecast_band = int(1260)
            case _:
                forecast_band = int(0)

        for dict in current_day_forecasts:
            if int(dict["$"]) == forecast_band:
                three_hour_forecast = dict

        weather_condition = str("")

        match three_hour_forecast["W"]:
            case '0':
                weather_condition = str("clear")
            case '1':
                weather_condition = str("sunny")
            case '2' | '3':
                weather_condition = str("partly cloudy")
            case '5':
                weather_condition = str("mist")
            case '6':
                weather_condition = str("fog")
            case '7':
                weather_condition = str("cloudy")
            case '8':
                weather_condition = str("overcast")
            case '9' | '10':
                weather_condition = str("light rain shower")
            case '11':
                weather_condition = str("drizzle")
            case '12':
                weather_condition = str("light rain")
            case '13' | '14':
                weather_condition = str("heavy rain shower")
            case '15':
                weather_condition = str("heavy rain")
            case '16' | '17':
                weather_condition = str("sleet shower")
            case '18':
                weather_condition = str("sleet")
            case '19' | '20':
                weather_condition = str("hail shower")
            case '21':
                weather_condition = str("hail")
            case '22' | '23':
                weather_condition = str("light snow shower")
            case '24':
                weather_condition = str("light snow")
            case '25' | '26':
                weather_condition = str("heavy snow shower")
            case '27':
                weather_condition = str("heavy snow")
            case '28' | '29':
                weather_condition = str("thunder shower")
            case '30':
                weather_condition = str("thunder")
            case _:
                weather_condition = str("")

        forecast = f'The current three hour forecast is {weather_condition} with a temperature of {three_hour_forecast["T"]} degrees celcius which feels like {three_hour_forecast["F"]} degrees celcius.  Wind speed is {three_hour_forecast["S"]} miles per hour with gusts up to {three_hour_forecast["G"]} miles per hour'

        return forecast


