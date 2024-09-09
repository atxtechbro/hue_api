import unittest
from unittest.mock import Mock, patch

from app.scenes_dynamo import get_user_preferences


class TestDynamoDBUserPreferences(unittest.TestCase):

    @patch('boto3.resource')  # Mock boto3 resource
    def test_missing_scene_preferences(self, mock_boto_resource):
        """
        Test that the default scene is returned when no scene preferences are found
        for the user in DynamoDB.
        """
        # Mock the DynamoDB Table get_item method
        mock_table = Mock()
        mock_boto_resource.return_value.Table.return_value = mock_table
        mock_table.get_item.return_value = {"Item": {"UserID": "user1", "scenes": {}}}

        # Expected default scene
        result = get_user_preferences("user1", "morning_scene")
        self.assertEqual(result['SceneName'], "default_scene")

    @patch('boto3.resource')  # Mock the boto3 resource
    def test_valid_scene_preferences(self, mock_boto_resource):
        """
        Test that the correct scene preferences are returned from DynamoDB.
        """
        # Mock the DynamoDB Table get_item method
        mock_table = Mock()
        mock_boto_resource.return_value.Table.return_value = mock_table
        mock_table.get_item.return_value = {
            "Item": {
                "UserID": "user1",
                "scenes": {
                    "morning_scene": {
                        "lights": [
                            {"light_id": 1, "state": {"on": True}},
                            {"light_id": 2, "state": {"on": True}}
                        ]
                    }
                }
            }
        }

        # Call the function with a valid scene
        result = get_user_preferences("user1", "morning_scene")
        
        # Check that the result matches the scene data
        expected_scene_data = {
            "lights": [
                {"light_id": 1, "state": {"on": True}},
                {"light_id": 2, "state": {"on": True}}
            ]
        }
        self.assertEqual(result, expected_scene_data)

if __name__ == "__main__":
    unittest.main()
