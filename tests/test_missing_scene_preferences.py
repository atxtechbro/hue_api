import unittest
from unittest.mock import MagicMock, patch

from app.scenes_dynamo import get_user_preferences  # Adjust im


class TestMissingScenePreferences(unittest.TestCase):

    @patch('boto3.resource')  # Mock the DynamoDB resource
    def test_missing_scene_preferences(self, mock_boto_resource):
        """
        Test that a default scene is returned when the scene preferences are missing
        for the given user in DynamoDB.
        """
        # Create a mock table
        mock_table = MagicMock()
        mock_boto_resource.return_value.Table.return_value = mock_table
    
        # Simulate DynamoDB response with no item matching the given key
        mock_table.get_item.return_value = {'Item': None}
    
        # Expected default scene
        default_scene = {"SceneName": "default_scene", "lights": []}
    
        # Assert that get_user_preferences returns the default scene when no scene preferences are found
        result = get_user_preferences(user_id="user1", scene_name="work_from_home")
        self.assertEqual(result, default_scene)

    @patch('boto3.resource')  # Mock the DynamoDB resource
    def test_user_without_scenes_key(self, mock_boto_resource):
        """
        Test that the default scene is returned when the DynamoDB response includes
        user data with no scene preferences.
        """
        # Create a mock table
        mock_table = MagicMock()
        mock_boto_resource.return_value.Table.return_value = mock_table

        # Simulate DynamoDB response with user data having no scenes for the requested key
        mock_table.get_item.return_value = {'Item': {"UserID": "user1", "scenes": {}}}

        # Expected default scene
        default_scene = {"SceneName": "default_scene", "lights": []}

        # Call get_user_preferences
        result = get_user_preferences(user_id="user1", scene_name="work_from_home")

        # Assert that the SceneName in the result is 'default_scene'
        self.assertEqual(result.get("SceneName"), "default_scene")

if __name__ == '__main__':
    unittest.main()
