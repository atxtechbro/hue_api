import unittest
from unittest.mock import patch
from lambda_function import get_user_preferences

class TestMissingScenePreferences(unittest.TestCase):

    @patch('app.dynamodb.get_user_data')
    def test_missing_scene_preferences(self, mock_dynamodb):
        # Simulate user without scene preferences
        mock_dynamodb.return_value = {"user_id": "user1", "scenes": {}}
        with self.assertRaises(ValueError):
            get_user_preferences(user_id="user1")

if __name__ == '__main__':
    unittest.main()
