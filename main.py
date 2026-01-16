from weather_service import WeatherService
from telegram_bot import TelegramBot

from dotenv import load_dotenv
import time

def main():
    
    load_dotenv()
    telegram_bot = TelegramBot()
    weather_service = WeatherService()
    last_update_id = 0

    while True:
        try:
            data = telegram_bot.update_data(last_update_id)
            
            updates = data.get('result', [])
            
            for elem in updates:
                last_update_id = elem['update_id']
                
                # Get text from message
                message = elem.get('message')
                if not message or 'text' not in message:
                    continue

                chat_id = message['chat']['id']
                user_text = message['text']
                
                # Logic to process user message
                if user_text == "/start":
                    answer = "Enter city:"
                else:
                    # User asked for weather
                    answer = weather_service.get_weather(user_text)
                    
                # Send answer to user
                telegram_bot.send_message(chat_id, answer)

        except Exception as e:
            print(f"Error: {e}")
            time.sleep(10)


if __name__ == '__main__':
    try:
        main()    
    except KeyboardInterrupt:
        print('\nProgram stopted!')
