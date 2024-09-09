import unittest
from unittest.mock import MagicMock, patch

from app.scenes_dynamo import get_user_preferences


class TestInvalidUserPreferences(unittest.TestCase):

    @patch('boto3.resource')  # Mock the DynamoDB resource
    def test_missing_scene_preferences(self, mock_boto_resource):
        """
        Test when user preferences are missing or invalid in DynamoDB.
        """
        # Create a mock table
        mock_table = MagicMock()
        mock_boto_resource.return_value.Table.return_value = mock_table

        # Simulate DynamoDB response with no item
        mock_table.get_item.return_value = {'Item': None}
        
        # Expected default scene
        default_scene = {"SceneName": "default_scene", "lights": []}
        
        # Check if the default scene is returned
        result = get_user_preferences("user1", "work_from_home")
        self.assertEqual(result, default_scene)

    @patch('boto3.resource')  # Mock the DynamoDB resource
    def test_no_scenes_key_in_user_data(self, mock_boto_resource):
        """
        Test when the 'scenes' key is missing in the user data returned from DynamoDB.
        """
        # Create a mock table
        mock_table = MagicMock()
        mock_boto_resource.return_value.Table.return_value = mock_table
    
        # Simulate DynamoDB response with missing 'scenes' key
        mock_table.get_item.return_value = {
            'Item': {
                "UserID": "user1"  # No 'scenes' key present
            }
        }
    
        # Expected default scene
        expected_default_scene = {"SceneName": "default_scene", "lights": []}
    
        # Call get_user_preferences
        result = get_user_preferences("user1", "work_from_home")
    
        # Assert that the result is the default scene
        self.assertEqual(result, expected_default_scene)

    @patch('boto3.resource')  # Mock the DynamoDB resource
    def test_scene_not_found_in_user_preferences(self, mock_boto_resource):
        """
        Test when a requested scene is not found in the user's scene preferences.
        """
        # Create a mock table
        mock_table = MagicMock()
        mock_boto_resource.return_value.Table.return_value = mock_table
    
        # Simulate user data with scene preferences but missing the requested scene
        mock_table.get_item.return_value = {
            "Item": {
                "UserID": "user1",
                "scenes": {
                    "wind_down_scene": {
                        "lights": [{"light_id": 1, "state": {"on": True, "bri": 200}}]
                    }
                }
            }
        }
    
        # Expected default scene
        expected_default_scene = {"SceneName": "default_scene", "lights": []}
    
        # Test for a non-existent scene
        result = get_user_preferences("user1", "work_from_home")
        self.assertEqual(result, expected_default_scene)

if __name__ == "__main__":
    unittest.main()
