
class Weather:
    def __init__(self, data):
        self.city = data.get('name', 'Unknown city')
        self.temperature = data['main']['temp']
        if data.get('weather'):
            self.weather_state = data['weather'][0].get('main', 'No data')
        else:
            self.weather_state = 'No data'
        
    def __str__(self):
        return (f"The weather in {self.city}:\n"
                f"Temp is {self.temperature}°C,\n"
                f"State is {self.weather_state}")
