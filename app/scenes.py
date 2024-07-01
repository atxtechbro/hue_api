import time

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
    """
    Creates a vibrant light show optimized for the song "La Pollera Colora" by Wilson Choperena.
    
    The light show starts with a fast-paced sequence of color changes to match the energetic
    beat of the song, then transitions to a pulsating pattern for the remainder of the song,
    featuring iconic Colombian colors.
    
    Parameters:
        api (HueAPI): The HueAPI instance to control the lights.
    """
    lights = api.get_lights()
    colors = [
        {"hue": 0, "sat": 254, "bri": 254},      # Red
        {"hue": 21845, "sat": 254, "bri": 254},  # Green
        {"hue": 43690, "sat": 254, "bri": 254},  # Blue
        {"hue": 10922, "sat": 254, "bri": 254},  # Yellow
    ]

    # Fast-paced sequence for the first part of the song
    fast_sequence_duration = 60  # Duration of the fast sequence in seconds
    fast_interval = 0.25  # Interval between color changes

    start_time = time.time()
    while time.time() - start_time < fast_sequence_duration:
        for color in colors:
            for light_id in lights:
                api.set_light_state(light_id, {**color, "on": True})
            time.sleep(fast_interval)

    # Pulsating pattern for the remainder of the song
    pulsate_sequence_duration = 120  # Duration of the pulsate sequence in seconds
    pulsate_interval = 1  # Interval for the pulsating effect

    pulsate_colors = [
        {"hue": 0, "sat": 254, "bri": 254},      # Red
        {"hue": 21845, "sat": 254, "bri": 254},  # Green
    ]

    start_time = time.time()
    while time.time() - start_time < pulsate_sequence_duration:
        for color in pulsate_colors:
            for light_id in lights:
                api.set_light_state(light_id, {**color, "bri": 254, "on": True})
            time.sleep(pulsate_interval)
            for light_id in lights:
                api.set_light_state(light_id, {**color, "bri": 100, "on": True})
            time.sleep(pulsate_interval)

