import json
import os

import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class HueAPI:
    """
    A class to interact with Philips Hue Bridge via its API.

    Attributes:
        bridge_ip (str): IP address of the Hue Bridge.
        username (str): The Hue API username for authentication.
    """
    
    def __init__(self):
        self.bridge_ip = os.getenv('bridge_ip')
        self.username = os.getenv('hue_username')
        if not self.bridge_ip or not self.username:
            raise ValueError("Missing environment variables for bridge IP or username")
        self.base_url = f'http://{self.bridge_ip}/api/{self.username}'

    def set_light_state(self, light_id, action):
        """
        Control the state of a specific light (on or off).
        """
        state = {"on": True} if action == "on" else {"on": False}
        url = f'{self.base_url}/lights/{light_id}/state'
        response = requests.put(url, json=state)
        return response.status_code == 200


    def get_light_state(self, light_id):
        """
        Fetch the current state of a specific light.

        Parameters:
            light_id (int): ID of the light to fetch.
        
        Returns:
            dict: JSON response of the light's state or an error message.
        """
        response = requests.get(f'{self.base_url}/lights/{light_id}')
        if response.status_code == 200:
            return response.json()
        else:
            return {'error': f"Failed to get state for light {light_id}, Error: {response.status_code}"}

    def get_lights(self):
        """
        Fetch the list of all lights connected to the Hue Bridge.

        Returns:
            dict: JSON response of all lights or an error message.
        """
        response = requests.get(f'{self.base_url}/lights')
        if response.status_code == 200:
            return response.json()
        else:
            return {'error': 'Failed to fetch lights list'}
