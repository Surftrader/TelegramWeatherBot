
class Weather:
    """
    A model class for storing and formatting weather data.
    
    Converts the JSON response from the OpenWeather API into a readable object.
    """
    
    def __init__(self, data):
        """
        Initializes the weather object.

        Args:
            data (dict): JSON-response from the OpenWeather API.
        """
        self.city = data.get('name', 'Unknown city')
        self.temperature = data['main']['temp']
        if data.get('weather'):
            self.weather_state = data['weather'][0].get('main', 'No data')
        else:
            self.weather_state = 'No data'
        
    def __str__(self):
        """
        Returns a string representation of the weather to send to the user.
        """
        return (f"The weather in {self.city}:\n"
                f"Temp is {self.temperature}°C,\n"
                f"State is {self.weather_state}")
