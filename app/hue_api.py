import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class HueAPI:
    def __init__(self):
        self.bridge_ip = os.getenv('bridge_ip')
        self.username = os.getenv('username')
        if not self.bridge_ip or not self.username:
            raise ValueError("Missing environment variables for bridge IP or username")
        self.base_url = f'http://{self.bridge_ip}/api/{self.username}'

    def get_lights(self):
        response = requests.get(f'{self.base_url}/lights')
        return response.json()

    def set_light_state(self, light_id, state):
        response = requests.put(f'{self.base_url}/lights/{light_id}/state', json=state)
        return response.json()
