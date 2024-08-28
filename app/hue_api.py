import requests
import os
from dotenv import load_dotenv
from app.circadian import get_circadian_lighting

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

    def set_light_state(self, scene_name):
        """
        Set the light state based on a given scene name.
        Maps a scene name to light settings (light_id and state).
        """
        # Example mapping from scene name to light settings
        scene_map = {
            'wind_down_scene': {'light_id': 1, 'state': {'on': True, 'bri': 100, 'ct': 500}},
            'work_from_home_scene': {'light_id': 2, 'state': {'on': True, 'bri': 254, 'ct': 370}},
            # Add more scenes as needed
        }
        
        if scene_name in scene_map:
            light_id = scene_map[scene_name]['light_id']
            state = scene_map[scene_name]['state']
            response = requests.put(f'{self.base_url}/lights/{light_id}/state', json=state)
            return response.json()
        else:
            return {'error': 'Scene not found'}

    def set_circadian_lighting(self):
        """
        Set circadian lighting for all lights.
        Uses get_circadian_lighting to determine light settings.
        """
        light_settings = get_circadian_lighting()
        # Assuming light_settings is a dictionary of {light_id: state}
        for light_id, state in light_settings.items():
            self.set_light_state(light_id, state)
        return {'status': 'Circadian lighting set successfully'}
