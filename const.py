####### WEATHER #######
WEATHER_URL = 'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={token}'

####### TELEGRAM #######
TELEGRAM_URL = 'https://api.telegram.org/bot{token}/{method}'
# Methods
UPDATES_METHOD = 'getUpdates'
SEND_METHOD = 'sendMessage'

UPDATE_ID_PATH = 'update_id'
with open(UPDATE_ID_PATH) as file:
    data = file.readline()
    if data:
        data = int(data)
    UPDATE_ID = data

