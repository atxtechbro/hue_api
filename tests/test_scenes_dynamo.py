import unittest
from unittest.mock import patch

from app.scenes_dynamo import activate_scene_group, get_user_preferences_with_cache


class TestSceneFallbacksAndGroups(unittest.TestCase):

    @patch('app.scenes_dynamo.get_user_preferences')
    def test_fallback_to_default_scene(self, mock_get_user_preferences):
        # Simulate missing scene, expect fallback
        mock_get_user_preferences.return_value = {"SceneName": "default_scene"}
        preferences = get_user_preferences_with_cache("user1", "work_from_home", time_of_day="21:00")
        self.assertEqual(preferences['SceneName'], "default_scene")

    @patch('app.scenes_dynamo.activate_scene')
    @patch('boto3.resource')  # Mock the DynamoDB resource
    def test_activate_scene_group(self, mock_boto_resource, mock_activate_scene):
        # Simulate a valid group of scenes
        mock_boto_resource.return_value.Table.return_value.query.return_value = {
            'Items': [
                {"SceneName": "morning_scene"},
                {"SceneName": "evening_scene"}
            ]
        }
        activate_scene_group("user1", "evening_group")
        mock_activate_scene.assert_any_call("user1", "morning_scene")
        mock_activate_scene.assert_any_call("user1", "evening_scene")

if __name__ == '__main__':
    unittest.main()
