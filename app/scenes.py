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
