import requests


def set_light_state(access_token, light_id, action):
    """
    Set the state of a specific light (on or off) using the Philips Hue Cloud API.
    """
    state = {"on": True} if action == "on" else {"on": False}
    url = f'https://api.meethue.com/bridge/{light_id}/lights/state'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    
    response = requests.put(url, json=state, headers=headers)
    if response.status_code == 200:
        print(f"Successfully turned {action} light {light_id}")
        return True
    else:
        print(f"Failed to turn {action} light {light_id}, response: {response.json()}")
        return False
