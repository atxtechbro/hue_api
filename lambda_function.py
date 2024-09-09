import json

from app.hue_cloud import set_light_state
from app.secrets_manager import get_secret


def lambda_handler(event, context):
    """
    AWS Lambda handler to control Philips Hue lights via the Cloud API.
    The event contains the action (on/off) and the light IDs to control.
    """
    # Retrieve the access_token from AWS Secrets Manager
    secret = get_secret("hue-api/oauth")
    access_token = secret['access_token']  # Assuming you've stored it as access_token

    # Extract action (on/off) from the event payload, default is "on"
    action = event.get("action", "on")
    
    # Extract the list of light IDs from the event payload
    lights = event.get("lights", [])  # e.g., [1, 2]
    
    if not lights:
        return {
            'statusCode': 400,
            'body': json.dumps("No lights specified in the request.")
        }
    
    # Set the state of all lights in the list
    success = True
    for light_id in lights:
        result = set_light_state(access_token, light_id, action)
        if not result:
            success = False
    
    # Return the response based on whether all lights were successfully controlled
    if success:
        return {
            'statusCode': 200,
            'body': json.dumps(f"All specified lights turned {action} successfully!")
        }
    else:
        return {
            'statusCode': 500,
            'body': json.dumps(f"Failed to turn {action} all specified lights.")
        }
