import os

import requests
from dotenv import load_dotenv

from app.circadian import get_circadian_lighting

# Load environment variables from .env file
load_dotenv()

class HueAPI:
    def __init__(self):
        self.bridge_ip = os.getenv('bridge_ip')
        self.username = os.getenv('hue_username')
        print(f"Bridge IP: {self.bridge_ip}")
        print(f"Username: {self.username}")
        if not self.bridge_ip or not self.username:
            raise ValueError("Missing environment variables for bridge IP or username")
        self.base_url = f'http://{self.bridge_ip}/api/{self.username}'
        
        # Define the scene map inside the constructor or at the class level
        self.scene_map = {
            'wind_down_scene': {
                'lights': [
                    {'light_id': 1, 'state': {'on': True, 'bri': 100, 'ct': 500}},
                    {'light_id': 2, 'state': {'on': True, 'bri': 100, 'ct': 500}}
                ]
            },
            'work_from_home_scene': {
                'lights': [
                    {'light_id': 1, 'state': {'on': True, 'bri': 254, 'ct': 370}},
                    {'light_id': 2, 'state': {'on': True, 'bri': 254, 'ct': 370}}
                ]
            }
        }

    def set_light_state(self, scene_name):
        """
        Set the light state based on a given scene name.
        Maps a scene name to light settings (light_id and state).
        """
        if scene_name in self.scene_map:
            for light in self.scene_map[scene_name]['lights']:
                light_id = light['light_id']
                state = light['state']
                response = requests.put(f'{self.base_url}/lights/{light_id}/state', json=state)
                print(f"Sending request to {self.base_url}/lights/{light_id}/state with state: {state}")
                print(f"API Response for Light {light_id}: {response.status_code}, {response.json()}")
            return {'status': 'All lights updated successfully'}
        else:
            return {'error': 'Scene not found'}

    def set_circadian_lighting(self):
        """
        Automatically sets the appropriate scene based on circadian lighting.
        """
        scene_name = get_circadian_lighting()  # Get the scene name based on the current time
        print(f"Activating scene: {scene_name}")
        response = self.set_light_state(scene_name)
        return {'status': f'{scene_name} activated successfully'}

    def get_light_state(self, light_id):
        """Fetch the current state of a specific light."""
        response = requests.get(f'{self.base_url}/lights/{light_id}')
        if response.status_code == 200:
            return response.json()
        else:
            return {'error': f"Failed to get state for light {light_id}"}
