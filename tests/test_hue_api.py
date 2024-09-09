import unittest
from unittest.mock import MagicMock, patch

from app.hue_api import HueAPI


class TestHueAPI(unittest.TestCase):
    def setUp(self):
        self.api = HueAPI()

    @patch('app.hue_api.requests.put')
    def test_set_light_state(self, mock_put):
        """Test setting light state for a light."""
        # Mock the response to return a status code of 200 (indicating success)
        mock_put.return_value.status_code = 200
        mock_put.return_value.json = MagicMock(return_value={"success": True})

        # Test turning a light on (light_id=1, action="on")
        response = self.api.set_light_state(1, "on")

        # Assert that the correct payload was sent
        mock_put.assert_called_once()  # Check that the put request was called once
        args, kwargs = mock_put.call_args  # Get the args and kwargs of the call
        self.assertIn('json', kwargs)  # Ensure the payload is in the kwargs
        self.assertEqual(kwargs['json'], {"on": True})  # Check if the correct payload was sent

        # Verify that the response was successful (should return True for status code 200)
        self.assertTrue(response)


if __name__ == '__main__':
    unittest.main()
