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

def chill_soccer_game_night(api):
    """
    Sets a chill light theme for watching the Colombia vs Brazil soccer game.
    The lights will use a Colombian color palette but maintain a consistent, cozy ambiance.

    Parameters:
        api (HueAPI): The HueAPI instance to control the lights.
    """
    lights = api.get_lights()
    
    # Define Colombian colors with a chill brightness level
    colors = [
        {"hue": 10922, "sat": 144, "bri": 100},  # Yellow
        {"hue": 0, "sat": 144, "bri": 100},      # Red
        {"hue": 43690, "sat": 144, "bri": 100},  # Blue
    ]

    # Set lights to Colombian colors with chill brightness
    for i, light_id in enumerate(lights):
        color = colors[i % len(colors)]
        api.set_light_state(light_id, {**color, "on": True})

def colombia_goal_celebration(api):
    """
    Creates a light show to celebrate a goal by Colombia.

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

    # Fast-paced sequence for celebration
    sequence_duration = 10  # Duration of the sequence in seconds
    interval = 0.5  # Interval between color changes

    start_time = time.time()
    while time.time() - start_time < sequence_duration:
        for color in colors:
            for light_id in lights:
                api.set_light_state(light_id, {**color, "on": True})
            time.sleep(interval)

def brazil_goal_celebration(api):
    """
    Creates a light show to celebrate a goal by Brazil.

    Parameters:
        api (HueAPI): The HueAPI instance to control the lights.
    """
    lights = api.get_lights()
    colors = [
        {"hue": 25500, "sat": 254, "bri": 254},  # Green
        {"hue": 10922, "sat": 254, "bri": 254},  # Yellow
    ]

    # Fast-paced sequence for celebration
    sequence_duration = 10  # Duration of the sequence in seconds
    interval = 0.5  # Interval between color changes

    start_time = time.time()
    while time.time() - start_time < sequence_duration:
        for color in colors:
            for light_id in lights:
                api.set_light_state(light_id, {**color, "on": True})
            time.sleep(interval)
