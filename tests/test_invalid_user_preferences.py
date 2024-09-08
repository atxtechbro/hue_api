import unittest
from unittest.mock import patch
from lambda_function import get_user_preferences

class TestInvalidUserPreferences(unittest.TestCase):

    @patch('app.dynamodb.get_user_data')
    def test_invalid_user_preferences(self, mock_dynamodb):
        # Simulate a missing user preference
        mock_dynamodb.return_value = None
        with self.assertRaises(ValueError):
            get_user_preferences(user_id="invalid_user")

if __name__ == '__main__':
    unittest.main()
