import unittest

from app.hue_api import HueAPI

class TestHueAPI(unittest.TestCase):
    def setUp(self):
        self.api = HueAPI()

    def test_get_lights(self):
        lights = self.api.get_lights()
        self.assertIsInstance(lights, dict)

if __name__ == '__main__':
    unittest.main()
