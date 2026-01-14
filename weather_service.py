import requests
import os

import const
from weather import Weather


class WeatherService:
    
    def __init__(self):
        self.token = os.getenv('WEATHER_TOKEN')
        self.base_url = const.WEATHER_URL

    def get_weather(self, city):
        params = {
            'q': city,
            'appid': self.token,
            'units': 'metric'
        }
        try:
            response = requests.get(self.base_url, params=params, timeout=10)
            
            if response.status_code == 404:
                return 'city not found'
            
            response.raise_for_status()
            
            data = response.json()
            
            return Weather(data)

        except Exception as e:
            return f"Network error: {e}"
