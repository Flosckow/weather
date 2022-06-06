
import json
import urllib.request
from config import API_YANDEX_KEY
import requests

def get_weather_here(coord) -> json:
    t = requests.get(url=f'https://api.weather.yandex.ru/v2/informers?lat={coord.latitude}&lon={coord.longtitude}&lang=ru_RU', headers={'X-Yandex-API-Key': 'fe4c93d8-ab25-4c6c-bb9e-61bcda184408'})
    print(t)
   
    

get_weather_here()