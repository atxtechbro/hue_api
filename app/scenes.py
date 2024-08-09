def wind_down_scene(api):
    lights = api.get_lights()
    for light_id in lights:
        api.set_light_state(light_id, {"on": True, "bri": 50, "hue": 10000, "sat": 144})

def work_from_home_scene(api):
    lights = api.get_lights()
    for light_id in lights:
        api.set_light_state(light_id, {"on": True, "bri": 254, "hue": 34495, "sat": 144})
