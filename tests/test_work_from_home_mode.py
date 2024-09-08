import pytest
from lambda_function import get_current_scene
from unittest.mock import patch
from datetime import time

@patch('app.hue_api.HueAPI.set_light_state')
def test_work_from_home_mode(mock_datetime):
    # Simulate 9 AM
    mock_datetime.now.return_value.time.return_value = time(9, 0)
    time_of_day = time(9, 0)  # Simulate the time_of_day argument
    scene = get_current_scene(time_of_day)

