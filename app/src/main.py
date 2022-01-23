import requests
import json

from pprint import pprint

class Weather():

    config = json.load(open("app/config/api_key.json"))
    url = 'http://api.openweathermap.org/data/2.5/weather?&%s&units=metric&lang=pl' % config.get('API_Key')
        
    def showWeather(self, city="Gdańsk"): 
        self.city = city
        r = requests.get(self.url + '&q=' + self.city)
        weather = json.loads(r.text)

        #Check if we had a failture
        if weather['cod'] != 200:
            raise Exception(weather['message'])

        pprint(weather)


# print(weather_data['city'])
# print(weather_data.get('city').get('name'))
# print(weather_data.get('city').get('main').get('temp'))

test = Weather()
test.showWeather('London')


















# logger.debug("debug message")
# logger.info("info message")
# logger.warning("warning message")
# logger.error("error message")
# logger.critical("critical message")