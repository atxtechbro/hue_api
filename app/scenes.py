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

def soccer_game_night(api):
    """
    Sets a cozy and fun light theme for watching the Colombia vs Brazil soccer game.
    The lights will change colors to represent the teams and celebrate goals.

    Parameters:
        api (HueAPI): The HueAPI instance to control the lights.
    """
    lights = api.get_lights()
    
    # Set initial cozy ambiance
    for light_id in lights:
        api.set_light_state(light_id, {"on": True, "bri": 150, "hue": 34495, "sat": 144})  # Greenish hue for a cozy atmosphere
    
    # Define goal celebration colors for Colombia and Brazil
    colombia_colors = [
        {"hue": 10922, "sat": 254, "bri": 254},  # Yellow
        {"hue": 0, "sat": 254, "bri": 254},      # Red
        {"hue": 43690, "sat": 254, "bri": 254},  # Blue
    ]
    
    brazil_colors = [
        {"hue": 21845, "sat": 254, "bri": 254},  # Green
        {"hue": 10922, "sat": 254, "bri": 254},  # Yellow
        {"hue": 43690, "sat": 254, "bri": 254},  # Blue
    ]
    
    def celebrate_goal(team_colors):
        """
        Celebrate a goal with a light show.

        Parameters:
            team_colors (list): List of color states to cycle through for the celebration.
        """
        celebration_duration = 10  # Duration of the celebration in seconds
        interval = 0.5  # Interval between color changes
        
        start_time = time.time()
        while time.time() - start_time < celebration_duration:
            for color in team_colors:
                for light_id in lights:
                    api.set_light_state(light_id, {**color, "on": True})
                time.sleep(interval)

    # Simulate goal events (replace this with actual event detection logic)
    # Example of celebrating a goal for Colombia
    celebrate_goal(colombia_colors)
    # Example of celebrating a goal for Brazil
    celebrate_goal(brazil_colors)

def celebrate_goal(api, team_colors):
    """
    Celebrate a goal with a light show.

    Parameters:
        api (HueAPI): The HueAPI instance to control the lights.
        team_colors (list): List of color states to cycle through for the celebration.
    """
    lights = api.get_lights()
    celebration_duration = 10  # Duration of the celebration in seconds
    interval = 0.5  # Interval between color changes
    
    start_time = time.time()
    while time.time() - start_time < celebration_duration:
        for color in team_colors:
            for light_id in lights:
                api.set_light_state(light_id, {**color, "on": True})
            time.sleep(interval)
