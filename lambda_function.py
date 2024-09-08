import json

import boto3

from app.dynamodb import get_user_data
from app.hue_api import HueAPI


def get_secret(secret_name, region_name="us-east-2"):
    client = boto3.client('secretsmanager', region_name=region_name)
    
    try:
        response = client.get_secret_value(SecretId=secret_name)
        return response['SecretString']
    except Exception as e:
        print(f"Error retrieving secret: {e}")
        raise e

def lambda_handler(event, context):
    # Retrieve the secrets
    bridge_ip = get_secret("hue-api/bridge-ip")
    hue_username = get_secret("hue-api/username")
    
    # Simulate time of day from event payload (e.g., "21:00")
    time_of_day = event.get("time_of_day", "09:00")  # Default to 09:00 if no time provided
    print(f"Simulated time of day: {time_of_day}")
    
    # Initialize the HueAPI with the secrets
    api = HueAPI()
    api.bridge_ip = bridge_ip  # Set the bridge IP
    api.username = hue_username  # Set the username
    
    # Set the light scene based on the time of day
    if time_of_day == "09:00":
        scene_name = "work_from_home_scene"
    elif time_of_day == "21:00":
        scene_name = "wind_down_scene"
    else:
        scene_name = None

    if scene_name:
        response = api.set_light_state(scene_name)
        return {
            'statusCode': 200,
            'body': json.dumps(f"Lighting scene '{scene_name}' activated successfully!")
        }
    else:
        return {
            'statusCode': 400,
            'body': json.dumps(f"Invalid time of day '{time_of_day}'. No lighting scene activated.")
        }

def get_user_preferences(user_id):
    user_data = get_user_data(user_id)
    if user_data is None:
        raise ValueError("User preferences not found")
    return user_data

def get_current_scene(time_of_day):
    # Add logic to determine the current scene based on the time of day
    if time_of_day == "09:00":
        return {"brightness": 100, "color": "cool_white"}
    elif time_of_day == "21:00":
        return {"brightness": 50, "color": "warm_white"}
    else:
        return None
