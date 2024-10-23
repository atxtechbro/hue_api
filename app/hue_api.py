# File: app\hue_api.py
import json
import logging
import os

import requests
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

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
            logger.error("Missing environment variables for bridge IP or username")
            raise ValueError("Missing environment variables for bridge IP or username")
        self.base_url = f'http://{self.bridge_ip}/api/{self.username}'

    def set_light_state(self, light_id, action):
        """
        Control the state of a specific light (on or off).
        """
        state = {"on": True} if action == "on" else {"on": False}
        url = f'{self.base_url}/lights/{light_id}/state'
        try:
            response = requests.put(url, json=state)
            response.raise_for_status()
            logger.info(f"Successfully set state for light {light_id}: {state}")
            return True
        except requests.exceptions.HTTPError as http_err:
            logger.error(f"HTTP error occurred while setting state for light {light_id}: {http_err} - Response: {response.text}")
            return False
        except requests.exceptions.RequestException as req_err:
            logger.error(f"Request exception while setting state for light {light_id}: {req_err}")
            return False

    def get_light_state(self, light_id):
        """
        Fetch the current state of a specific light.

        Parameters:
            light_id (int): ID of the light to fetch.
        
        Returns:
            dict: JSON response of the light's state or an error message.
        """
        url = f'{self.base_url}/lights/{light_id}'
        try:
            response = requests.get(url)
            response.raise_for_status()
            logger.info(f"Successfully fetched state for light {light_id}")
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            logger.error(f"HTTP error occurred while fetching state for light {light_id}: {http_err} - Response: {response.text}")
            return {'error': f"Failed to get state for light {light_id}, Error: {response.status_code}"}
        except requests.exceptions.RequestException as req_err:
            logger.error(f"Request exception while fetching state for light {light_id}: {req_err}")
            return {'error': f"Failed to get state for light {light_id}, Error: {req_err}"}

    def get_lights(self):
        """
        Fetch the list of all lights connected to the Hue Bridge.

        Returns:
            dict: JSON response of all lights or an error message.
        """
        url = f'{self.base_url}/lights'
        try:
            response = requests.get(url)
            response.raise_for_status()
            logger.info("Successfully fetched list of lights")
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            logger.error(f"HTTP error occurred while fetching lights list: {http_err} - Response: {response.text}")
            return {'error': 'Failed to fetch lights list'}
        except requests.exceptions.RequestException as req_err:
            logger.error(f"Request exception while fetching lights list: {req_err}")
            return {'error': 'Failed to fetch lights list'}
