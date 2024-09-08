import unittest
from unittest.mock import patch
from app.circadian import get_circadian_lighting
from datetime import time

class TestCircadianLighting(unittest.TestCase):

    @patch('app.circadian.datetime')
    def test_get_circadian_lighting_morning(self, mock_datetime):
        """Test circadian lighting settings for morning time."""
        mock_datetime.now.return_value.time.return_value = time(8, 0)
        result = get_circadian_lighting()
        self.assertEqual(result, 'wind_down_scene')

    @patch('app.circadian.datetime')
    def test_get_circadian_lighting_afternoon(self, mock_datetime):
        """Test circadian lighting settings for afternoon time."""
        mock_datetime.now.return_value.time.return_value = time(15, 0)
        result = get_circadian_lighting()
        self.assertEqual(result, 'work_from_home_scene')

    @patch('app.circadian.datetime')
    def test_get_circadian_lighting_evening(self, mock_datetime):
        """Test circadian lighting settings for evening time."""
        mock_datetime.now.return_value.time.return_value = time(20, 0)
        result = get_circadian_lighting()
        self.assertEqual(result, 'wind_down_scene')

if __name__ == '__main__':
    unittest.main()
