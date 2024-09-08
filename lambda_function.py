import json
from app.dynamodb import get_user_data
import boto3


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
    
    # Your circadian lighting logic here
    # Example: print the retrieved secrets (remove in production)
    print(f"Bridge IP: {bridge_ip}, Hue Username: {hue_username}")
    
    # Assuming you have logic to control the lighting here

    return {
        'statusCode': 200,
        'body': json.dumps('Circadian lighting automation triggered!')
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
