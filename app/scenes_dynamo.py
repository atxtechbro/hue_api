# File: app\scenes_dynamo.py

import json
import logging
import os
import time
from decimal import Decimal

import boto3
import requests
from boto3.dynamodb.conditions import Key
from boto3.dynamodb.types import TypeDeserializer

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# In-memory cache for frequently accessed scenes
scene_cache = {}

# Create a TypeDeserializer instance
deserializer = TypeDeserializer()

def deserialize_item(item):
    """Recursively deserialize DynamoDB items to native Python types."""
    if isinstance(item, dict):
        if len(item) == 1:
            try:
                # Attempt to deserialize using TypeDeserializer
                return deserializer.deserialize(item)
            except Exception:
                pass  # Not a DynamoDB-typed dict, proceed to deserialize normally
        # Regular dictionary, recursively deserialize its values
        return {k: deserialize_item(v) for k, v in item.items()}
    elif isinstance(item, list):
        # Recursively deserialize each item in the list
        return [deserialize_item(i) for i in item]
    else:
        # Base case: return the item as is (primitive type)
        return item

def convert_decimals(obj):
    """
    Recursively convert Decimal instances to int or float.
    
    Args:
        obj: The object to convert.
    
    Returns:
        The converted object with Decimals as int or float.
    """
    if isinstance(obj, dict):
        return {k: convert_decimals(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [convert_decimals(i) for i in obj]
    elif isinstance(obj, Decimal):
        if obj % 1 == 0:
            return int(obj)
        else:
            return float(obj)
    else:
        return obj

def get_user_preferences(user_id, scene_name, time_of_day=None):
    """
    Retrieves the user's lighting preferences for a specific scene from DynamoDB.
    Falls back to a default scene if none is found.
    """
    dynamodb = boto3.resource('dynamodb', region_name='us-east-2')
    table = dynamodb.Table('LightingPreferences')

    key = {'UserID': user_id, 'SceneName': scene_name}
    if time_of_day:
        key['TimeOfDay'] = time_of_day  # Optional time-based filtering

    try:
        response = table.get_item(Key=key)
        item = response.get('Item')
    except Exception as e:
        logger.error(f"Error fetching scene '{scene_name}' for user '{user_id}': {e}")
        return {"SceneName": "default_scene", "lights": []}

    if item and 'scenes' in item and scene_name in item['scenes']:
        return deserialize_item(item['scenes'][scene_name])
    else:
        logger.warning(f"Scene '{scene_name}' not found for user '{user_id}', falling back to default_scene")
        return {"SceneName": "default_scene", "lights": []}

def activate_scene(user_id, scene_name):
    """
    Activates a scene by sending state updates for all lights to the Hue Bridge.
    """
    dynamodb = boto3.resource('dynamodb', region_name='us-east-2')
    table = dynamodb.Table('LightingPreferences')

    # Retrieve the scene from DynamoDB
    try:
        response = table.get_item(Key={'UserID': user_id, 'SceneName': scene_name})
        item = response.get('Item')
    except Exception as e:
        logger.error(f"Error fetching scene '{scene_name}' for user '{user_id}': {e}")
        return False

    if not item:
        logger.warning(f"Scene '{scene_name}' not found for user '{user_id}'")
        return False

    # Deserialize the scene data correctly
    scene = deserialize_item(item['scenes'][scene_name])

    # Convert any remaining Decimals to int or float
    scene = convert_decimals(scene)

    try:
        scene_json = json.dumps(scene, indent=2)
        logger.info(f"Retrieved scene data:\n{scene_json}")
    except TypeError as e:
        logger.error(f"Serialization Error: {e}")
        return False

    bridge_ip = os.getenv('bridge_ip')
    username = os.getenv('hue_username')

    if not bridge_ip or not username:
        logger.error("Bridge IP or Hue username not set in environment variables.")
        return False

    # Iterate through lights and send requests to the Hue Bridge
    failed_lights = []
    for light in scene.get('lights', []):
        light_id = light.get('light_id')
        state = light.get('state')

        if not light_id or not state:
            logger.warning(f"Invalid light configuration: {light}")
            continue

        logger.info(f"Setting state for light {light_id}: {state}")

        url = f"http://{bridge_ip}/api/{username}/lights/{light_id}/state"
        try:
            response = requests.put(url, json=state)
            response.raise_for_status()  # Raises HTTPError for bad responses
            logger.info(f"Light {light_id} response: {response.status_code} - {response.text}")
        except requests.exceptions.HTTPError as http_err:
            logger.error(f"HTTP error occurred for light {light_id}: {http_err} - Response: {response.text}")
            failed_lights.append(light_id)
            continue
        except requests.exceptions.RequestException as req_err:
            logger.error(f"Request exception for light {light_id}: {req_err}")
            failed_lights.append(light_id)
            continue

        time.sleep(0.2)  # Add a small delay between requests

    if failed_lights:
        logger.error(f"Failed to set state for lights: {failed_lights}")
        return False

    logger.info(f"All lights in scene '{scene_name}' activated successfully for user '{user_id}'.")
    return True

def activate_scene_group(user_id, group_name):
    """
    Activates all scenes within a group by querying DynamoDB for group-based scenes.
    """
    dynamodb = boto3.resource('dynamodb', region_name='us-east-2')
    table = dynamodb.Table('LightingPreferences')

    # Query by group
    try:
        response = table.query(
            IndexName="GroupIndex",
            KeyConditionExpression=Key('Group').eq(group_name)
        )
        scenes = response.get('Items', [])
    except Exception as e:
        logger.error(f"Error querying group '{group_name}': {e}")
        return

    if not scenes:
        logger.warning(f"No scenes found for group '{group_name}'")
        return

    for scene in scenes:
        # Deserialize each scene item
        deserialized_scene = deserialize_item(scene)
        scene_name = deserialized_scene.get('SceneName')
        if not scene_name:
            logger.warning(f"SceneName missing in scene: {scene}")
            continue
        activate_scene(user_id, scene_name)
