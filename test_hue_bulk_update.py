import time

import requests

bridge_ip = ""  # Replace with your bridge IP
username = ""  # Replace with your Hue username

lights = [1, 2, 3, 4, 5]
state = {"on": True, "bri": 200, "hue": 10000, "sat": 144}

for light_id in lights:
    url = f"http://{bridge_ip}/api/{username}/lights/{light_id}/state"
    response = requests.put(url, json=state)
    print(f"Light {light_id} response: {response.status_code} - {response.text}")
    time.sleep(0.2)  # Add a small delay between requests
