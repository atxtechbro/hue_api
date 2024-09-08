import pytest
from lambda_function import get_current_scene
from unittest.mock import patch
from datetime import time

@patch('app.hue_api.HueAPI.set_light_state')
def test_wind_down_scene(mock_datetime):
    # Simulate 9 PM
    mock_datetime.now.return_value.time.return_value = time(21, 0)
    time_of_day = time(21, 0)  # Simulate the time_of_day argument
    scene = get_current_scene(time_of_day)
