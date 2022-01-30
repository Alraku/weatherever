# -*- coding: UTF-8 -*-
import requests
import json
import datetime

from pprint import pprint
from types import SimpleNamespace
from custom_colors import CustomFormatter, Colors
from helpers import wind_direction


class Weather():

    def __init__(self):

        #Initialize logger in order to print formatted weather info
        self.logger = CustomFormatter().get_logger()

        self.config = json.load(open("config/config.json"), object_hook=lambda d: SimpleNamespace(**d))
        self.API_Key = json.load(open("config/api_key.json")).get('API_Key')

        self.url_city_name = f'http://api.openweathermap.org/data/2.5/weather?&{self.API_Key}&units={self.config.units}&lang={self.config.language}'
        self.url_coordinates = f'https://api.openweathermap.org/data/2.5/onecall?exclude=hourly,daily&{self.API_Key}&units={self.config.units}&lang={self.config.language}&lat=10.44&lon=-94.04'

    def request_weather(self, city):

        r = requests.get(self.url_city_name + '&q=' + city)
        weather = json.loads(r.text)

        #Check if we had a failture
        if weather['cod'] != 200:
            raise Exception(weather['message'])

        return weather

    def show_weather(self): 

        city = input('Enter name of the location: ')
        response = self.request_weather(city)
        weather_data = self.gather_data(response)
        self.format_output(weather_data)

    def show_weather_default(self): 

        city = 'Gdańsk'
        response = self.request_weather(city)
        weather_data = self.gather_data(response)
        self.format_output(weather_data)

    def gather_data(self, weather_response):

        #pprint(weather_response)
        weather_dict = {"city": weather_response.get('name'), 
                        "country": weather_response.get('sys').get('country'),
                        "temp": round(weather_response.get('main').get('temp'),1),
                        "weather": weather_response['weather'][0]['description'].title(),
                        "wind_speed": round(weather_response['wind']['speed']*3.6, 0),
                        "wind_direction": wind_direction(weather_response['wind']['deg']),
                        "wind_gust": round(weather_response.get('wind').get('gust', 0)*3.6, 0),
                        "feels_like": round(weather_response['main']['feels_like'],1),
                        "humidity": weather_response['main']['humidity'],
                        "pressure": weather_response['main']['pressure'],
                        "sunrise": datetime.datetime.fromtimestamp(weather_response['sys']['sunrise']).strftime('%H:%M'),
                        "sunset": datetime.datetime.fromtimestamp(weather_response['sys']['sunset']).strftime('%H:%M')}

        return weather_dict

    def format_output(self, WD):

        #pprint(WD)
        self.logger.info('')
        print("\n")
        print(f"{Colors.FG.RED}Location:{Colors.RESET} {WD.get('city')} ({WD.get('country')})")
        print(f"{Colors.FG.RED}Temperature:{Colors.RESET} {WD.get('temp')} °C")
        print(f"{Colors.FG.RED}Feels Like:{Colors.RESET} {WD.get('feels_like')} °C")
        print(f"{Colors.FG.RED}Conditions:{Colors.RESET} {WD.get('weather')}")
        print(f"{Colors.FG.RED}Humidity:{Colors.RESET} {WD.get('humidity')}%")
        print(f"{Colors.FG.RED}Pressure:{Colors.RESET} {WD.get('pressure')} hPa\n")
        print(f"{Colors.FG.RED}Wind:{Colors.RESET} {WD.get('wind_speed')} Km/h")
        print(f"{Colors.FG.RED}Wind Direction:{Colors.RESET} {WD.get('wind_direction')}")
        print(f"{Colors.FG.RED}Wind Gusts:{Colors.RESET} {WD.get('wind_gust')} Km/h\n")
        print(f"{Colors.FG.RED}Sunrise:{Colors.RESET} {WD.get('sunrise')}")
        print(f"{Colors.FG.RED}Sunset:{Colors.RESET} {WD.get('sunset')}")

#test = Weather()
#test.show_weather_default()
