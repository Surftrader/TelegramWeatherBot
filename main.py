import requests
import json
import time

from dotenv import load_dotenv
import os

import const


def answer_user_bot(data):
    data = {
        'chat_id': os.getenv('MY_ID'),
        'text': data
    }
    url = const.TELEGRAM_URL.format(
        token=os.getenv('TELEGRAM_TOKEN'), 
        method=const.SEND_METHOD
        )
    requests.post(url, data=data)

def parse_weathed_data(data):
    for elem in data['weather']:
        weather_state = elem['main']
    temp = round(data['main']['temp'] - 273.15, 2)
    city = data['name']
    msg = f'The weather in {city}: Temp is {temp}, State is {weather_state}.' 
    return msg


def get_weather(location):
    url = const.WEATHER_URL.format(
        city=location,
        token=os.getenv('WEATHER_TOKEN'))
    response = requests.get(url)
    if response.status_code != 200:
        return 'city not found'
    data = json.loads(response.content) 
    return parse_weathed_data(data)


def get_message(data):
    return data['message']['text']


def save_update_id(update):
    with open(const.UPDATE_ID_PATH , 'w') as file:
        file.write(str(update['update_id']))
        const.UPDATE_ID = update['update_id']
    return True


def main():
    while True:
        url = const.TELEGRAM_URL.format(
            token=os.getenv('TELEGRAM_TOKEN'), 
            method=const.UPDATES_METHOD)
        content = requests.get(url).text
        data = json.loads(content)
        
        result = data['result'][::-1]
        needed_part = None
        
        for elem in result:
            if elem['message']['chat']['id'] == int(os.getenv('MY_ID')):
                needed_part = elem
                break

        if const.UPDATE_ID != needed_part['update_id']:
            message = get_message(needed_part)
            weather = get_weather(message)
            answer_user_bot(weather)
            save_update_id(needed_part)

        # pause 5 seconds
        time.sleep(5) 


if __name__ == '__main__':
    try:
        load_dotenv()
        main()
    except KeyboardInterrupt:
        print('\nProgram stopted!')
