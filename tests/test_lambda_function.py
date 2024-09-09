import json
import unittest
from unittest.mock import patch

from lambda_function import lambda_handler


class TestLambdaTrigger(unittest.TestCase):

    @patch('app.secrets_manager.get_secret', return_value={'SecretString': '{"access_token": "mock-token"}'})
    @patch('app.hue_cloud.set_light_state', return_value=True)
    def test_lambda_trigger(self, mock_set_light_state, mock_get_secret):
        """Test the lambda trigger for turning lights on."""
        
        # Example event for lambda to trigger turning on the lights
        event = {'action': 'on', 'lights': [1, 2]}
        
        # Call the lambda handler function
        result = lambda_handler(event, None)
        
        # Check the result, adjust based on expected lambda_handler return value
        self.assertEqual(result['statusCode'], 200)
        self.assertEqual(result['body'], 'Lights turned on')  # Example check
    
    def test_json_decoding(self):
        json_string = '{"access_token": "mock-token"}'
        try:
            data = json.loads(json_string)
            print(data)
        except json.JSONDecodeError as e:
            print(f"JSON decoding failed: {e}")

if __name__ == "__main__":
    unittest.main()
