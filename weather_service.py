import requests
import os

import const
from weather import Weather


class WeatherService:
    """
    A service for working with the weather forecast API (OpenWeather).
    """
    
    def __init__(self):
        """
        Initializes the API URL and loads WEATHER_TOKEN from the environment.
        """
        self.token = os.getenv('WEATHER_TOKEN')
        self.base_url = const.WEATHER_URL

    def get_weather(self, city):
        """
        Gets the current weather for the specified city.
        
        Forms a request, handles errors (for example, if the city is not found), and returns a formatted string.

        Args:
            city (str): City name in English.

        Returns:
            str: The finished forecast text or error message.
        """
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
