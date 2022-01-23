import requests
import json

from pprint import pprint

class Weather():

    url = 'http://api.openweathermap.org/data/2.5/weather?&appid=fafa5ec8ced374a06b103d3c60e1b76d&units=metric&lang=pl'
        
    def showWeather(self, city="Gdańsk"): 
        self.city = city
        r = requests.get(self.url + '&q=' + self.city)
        weather = json.loads(r.text)
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