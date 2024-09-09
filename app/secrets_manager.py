import json

import boto3


def get_secret(secret_name, region_name="us-east-2"):
    """
    Retrieves secrets (like access_token) from AWS Secrets Manager.
    """
    client = boto3.client('secretsmanager', region_name=region_name)
    try:
        response = client.get_secret_value(SecretId=secret_name)
        secret_string = response['SecretString']
        return json.loads(secret_string)
    except Exception as e:
        print(f"Error retrieving secret: {e}")
        raise e
    