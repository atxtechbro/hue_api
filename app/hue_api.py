import requests

class HueAPI:
    def __init__(self, bridge_ip, username):
        self.bridge_ip = bridge_ip
        self.username = username
        self.base_url = f'http://{bridge_ip}/api/{username}'

    def get_lights(self):
        response = requests.get(f'{self.base_url}/lights')
        return response.json()

    def set_light_state(self, light_id, state):
        response = requests.put(f'{self.base_url}/lights/{light_id}/state', json=state)
        return response.json()


# Example usage:
bridge_ip = '192.168.1.2'  # Replace with your Philips Hue Bridge IP
username = 'newusername123456'  # Replace with your generated username

hue_api = HueAPI(bridge_ip, username)
lights = hue_api.get_lights()
print(lights)