import requests
import os

import const

class TelegramBot:
    """
    A class for interacting with the Telegram Bot API.
    
    Implements receiving updates via Long Polling and sending messages.
    """
    
    def __init__(self):
        """
        Initializes the bot's base URL using the TELEGRAM_TOKEN environment variable.
        """
        self.token = os.getenv('TELEGRAM_TOKEN')
        self.base_url = f"{const.TELEGRAM_URL}{self.token}/"
    
    
    def update_data(self, last_update_id):
        """
        Requests new messages from Telegram.
        
        Uses Long Polling (server-side wait).

        Args:
            last_update_id (int): ID of the last processed update.

        Returns:
            dict: JSON response with a list of new updates.
        """
        params = {'offset': last_update_id + 1, 'timeout': 30}
        try:
            content = requests.get(f"{self.base_url}{const.UPDATES_METHOD}", params=params)
            content.raise_for_status()
            data = content.json()
            
            if not data.get('ok'):
                print(f"Telegram API Error: {data.get('description')}")
                return {'result': []}
            
            return data
        except Exception as e:
            print(f"Network error: {e}")
            return {'result': []}
 
 
    def send_message(self, user_id, text):
        """
        Sends a text message to a specific user.

        Args:
            user_id (int): The user's chat ID.
            text (str): The message text.
        """
        data = {
            'chat_id': user_id,
            'text': text
        }
        requests.post(f"{self.base_url}{const.SEND_METHOD}", data=data, timeout=10)

