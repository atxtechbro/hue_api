import unittest
from unittest.mock import patch
from lambda_function import lambda_handler

class TestLambdaTrigger(unittest.TestCase):

    @patch('lambda_function.get_secret', return_value='mock-secret')
    @patch('app.hue_api.HueAPI.set_circadian_lighting')
    def test_lambda_trigger(self, mock_set_circadian_lighting, mock_get_secret):
        """Test the lambda trigger for circadian lighting."""
        
        # Mock the return value for set_circadian_lighting
        mock_set_circadian_lighting.return_value = {'status': 'success'}
        
        # Example event for lambda to trigger circadian lighting
        event = {'trigger': 'circadian_lighting'}
        
        # Call the lambda handler function
        result = lambda_handler(event, None)
        
        # Assert that the lambda function returned statusCode 200 and the expected body
        self.assertEqual(result['statusCode'], 200)
        self.assertIn('Circadian lighting automation triggered!', result['body'])

if __name__ == '__main__':
    unittest.main()
