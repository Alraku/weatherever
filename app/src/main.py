# -*- coding: UTF-8 -*-
import requests
import json

from pprint import pprint
from custom_logger import CustomFormatter

class Weather():

    def __init__(self):

        self.config = json.load(open("app/config/api_key.json"))
        API_Key = self.config.get('API_Key')
        self.url = f'http://api.openweathermap.org/data/2.5/weather?&{API_Key}&units=metric&lang=en'

    def request_weather(self, city):

        r = requests.get(self.url + '&q=' + city)
        weather = json.loads(r.text)

        #Check if we had a failture
        if weather['cod'] != 200:
            raise Exception(weather['message'])

        return weather

    def show_weather(self, city="Gdańsk"): 

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

test = Weather()
test.show_weather('Gdańsk')

