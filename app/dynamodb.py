import boto3


def get_user_data(user_id):
    """
    Fetch user data from DynamoDB for a given user ID.

    Args:
        user_id (str): The ID of the user.

    Returns:
        dict: The user data from DynamoDB or None if not found.
    """
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('LightingPreferences')

    try:
        response = table.get_item(Key={'UserID': user_id})
        return response.get('Item', None)
    except Exception as e:
        print(f"Error fetching user data: {e}")
        return None
