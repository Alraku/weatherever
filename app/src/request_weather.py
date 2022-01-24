# -*- coding: UTF-8 -*-
import requests
import json

from pprint import pprint
from types import SimpleNamespace
from custom_logger import CustomFormatter


class Weather():

    def __init__(self):

        self.config = json.load(open("app/config/config.json"), object_hook=lambda d: SimpleNamespace(**d))
        self.API_Key = json.load(open("app/config/api_key.json")).get('API_Key')

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
        response_weather = self.request_weather(city)
        self.format_output(response_weather)

    def show_weather_default(self): 

        city = 'Gdańsk'
        response_weather = self.request_weather(city)
        self.format_output(response_weather)

    def format_output(self, weather_response):

        #pprint(weather_response)
        weather_dict = {"city": weather_response.get('name'), 
                        "country": weather_response.get('sys').get('country'),
                        "temp": round(weather_response.get('main').get('temp'),1),
                        "weather": weather_response['weather'][0]['description']}

        logger = CustomFormatter().get_logger()
        logger.info('')
        logger.error("Current weather for location {city} ({country}) is {temp} Celsius and it is {weather}".format(**weather_dict))
