import boto3
from boto3.dynamodb.conditions import Key

# In-memory cache for frequently accessed scenes
scene_cache = {}

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

    response = table.get_item(Key=key)

    item = response.get('Item')
    
    # Check if the item exists and contains the requested scene
    if item and 'scenes' in item and scene_name in item['scenes']:
        return item['scenes'][scene_name]
    else:
        print(f"Scene {scene_name} not found for user {user_id}, falling back to default_scene")
        return {"SceneName": "default_scene", "lights": []}

def get_user_preferences_with_cache(user_id, scene_name, time_of_day=None):
    """
    Retrieves the user's lighting preferences from cache or DynamoDB.
    """
    cache_key = f"{user_id}_{scene_name}_{time_of_day}"
    if cache_key in scene_cache:
        return scene_cache[cache_key]

    # If not cached, retrieve from DynamoDB
    preferences = get_user_preferences(user_id, scene_name, time_of_day)
    
    # Cache the result for future queries
    scene_cache[cache_key] = preferences
    return preferences

def activate_scene(user_id, scene_name):
    """
    Activates a single scene by calling the Hue API.
    (You will need to implement the actual call to the Hue API here.)
    """
    # Logic to activate the scene via Hue API would go here
    print(f"Activating scene {scene_name} for user {user_id}")
    pass

def activate_scene_group(user_id, group_name):
    """
    Activates all scenes within a group by querying DynamoDB for group-based scenes.
    """
    dynamodb = boto3.resource('dynamodb', region_name='us-east-2')
    table = dynamodb.Table('LightingPreferences')

    # Query by group
    response = table.query(
        IndexName="GroupIndex",
        KeyConditionExpression=Key('Group').eq(group_name)
    )

    scenes = response.get('Items', [])
    if not scenes:
        print(f"No scenes found for group {group_name}")
        return

    for scene in scenes:
        activate_scene(user_id, scene['SceneName'])
