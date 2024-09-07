import json


def lambda_handler(event, context):
    # Returning a simple JSON response for testing purposes
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
