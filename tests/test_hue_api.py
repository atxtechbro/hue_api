import unittest
from unittest.mock import patch, MagicMock
from app.hue_api import HueAPI

class TestHueAPI(unittest.TestCase):
    def setUp(self):
        self.api = HueAPI()

    @patch('app.hue_api.requests.put')
    def test_set_light_state(self, mock_put):
        """Test setting light state for a scene."""
        mock_put.return_value.json = MagicMock(return_value={"success": True})
        
        # Test the wind_down_scene
        response = self.api.set_light_state('wind_down_scene')
        self.assertEqual(response['status'], 'All lights updated successfully')
        
        # Verify the requests.put was called twice (for 2 lights)
        self.assertEqual(mock_put.call_count, 2)

    @patch('app.hue_api.requests.put')
    def test_set_circadian_lighting(self, mock_put):
        """Test automatic setting of circadian lighting."""
        mock_put.return_value.json = MagicMock(return_value={"success": True})
        
        # Mock the get_circadian_lighting to return 'work_from_home_scene'
        with patch('app.hue_api.get_circadian_lighting', return_value='work_from_home_scene'):
            response = self.api.set_circadian_lighting()
            self.assertEqual(response['status'], 'work_from_home_scene activated successfully')
        
        # Verify the requests.put was called twice (for 2 lights)
        self.assertEqual(mock_put.call_count, 2)

if __name__ == '__main__':
    unittest.main()
