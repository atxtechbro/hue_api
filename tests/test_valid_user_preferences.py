import unittest
from unittest import TestCase
from unittest.mock import MagicMock, patch

from app.scenes_dynamo import get_user_preferences


class TestValidUserPreferences(TestCase):

    @patch('boto3.resource')  # Mock boto3 resource
    def test_valid_scene_preferences(self, mock_boto_resource):
        """
        Test retrieving valid user scene preferences from DynamoDB.
        """
        # Create a mock DynamoDB Table object
        mock_table = MagicMock()
        mock_boto_resource.return_value.Table.return_value = mock_table

        # Define the mock response for the get_item call
        mock_table.get_item.return_value = {
            'Item': {
                'user_id': 'user1',
                'scenes': {
                    'work_from_home': {
                        'lights': [{'light_id': 1, 'state': {'on': True, 'bri': 200}}]
                    }
                }
            }
        }

        # Call the function to test
        preferences = get_user_preferences('user1', 'work_from_home')

        # Verify that the correct preferences are returned
        self.assertEqual(preferences['lights'], [{'light_id': 1, 'state': {'on': True, 'bri': 200}}])

if __name__ == "__main__":
    unittest.main()
