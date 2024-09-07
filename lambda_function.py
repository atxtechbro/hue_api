import json

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
