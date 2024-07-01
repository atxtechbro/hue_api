import time
from hue_api import HueAPI

def romantic_scene(api):
    lights = api.get_lights()
    for light_id in lights:
        api.set_light_state(light_id, {"on": True, "bri": 144, "hue": 56100, "sat": 254})

def party_scene(api):
    lights = api.get_lights()
    for light_id in lights:
        api.set_light_state(light_id, {"on": True, "bri": 254, "hue": 10000, "sat": 254})

def stargazing_scene(api):
    lights = api.get_lights()
    for light_id in lights:
        api.set_light_state(light_id, {"on": True, "bri": 50, "hue": 47000, "sat": 254})

def wind_down_scene(api):
    lights = api.get_lights()
    for light_id in lights:
        api.set_light_state(light_id, {"on": True, "bri": 50, "hue": 10000, "sat": 144})

def work_from_home_scene(api):
    lights = api.get_lights()
    for light_id in lights:
        api.set_light_state(light_id, {"on": True, "bri": 254, "hue": 34495, "sat": 144})

def cumbia_light_show(api):
    lights = api.get_lights()
    colors = [
        {"hue": 0, "sat": 254, "bri": 254},   # Red
        {"hue": 21845, "sat": 254, "bri": 254}, # Green
        {"hue": 43690, "sat": 254, "bri": 254}, # Blue
        {"hue": 10922, "sat": 254, "bri": 254}, # Yellow
    ]

    for i in range(20):  # Run the sequence 20 times
        for color in colors:
            for light_id in lights:
                api.set_light_state(light_id, {**color, "on": True})
            time.sleep(0.5)  # Adjust timing as needed
