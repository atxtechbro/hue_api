import sys

from app.hue_api import HueAPI
from app.scenes import romantic_scene, party_scene, stargazing_scene, wind_down_scene, work_from_home_scene, soccer_game_night, celebrate_goal

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 cli.py <scene_name>")
        sys.exit(1)
    
    scene_name = sys.argv[1]
    api = HueAPI()

    if scene_name == "romantic_scene":
        romantic_scene(api)
    elif scene_name == "party_scene":
        party_scene(api)
    elif scene_name == "stargazing_scene":
        stargazing_scene(api)
    elif scene_name == "wind_down_scene":
        wind_down_scene(api)
    elif scene_name == "work_from_home_scene":
        work_from_home_scene(api)
    elif scene_name == "soccer_game_night":
        soccer_game_night(api)
    elif scene_name == "celebrate_colombia_goal":
        colombia_colors = [
            {"hue": 10922, "sat": 254, "bri": 254},  # Yellow
            {"hue": 0, "sat": 254, "bri": 254},      # Red
            {"hue": 43690, "sat": 254, "bri": 254},  # Blue
        ]
        celebrate_goal(api, colombia_colors)
    elif scene_name == "celebrate_brazil_goal":
        brazil_colors = [
            {"hue": 21845, "sat": 254, "bri": 254},  # Green
            {"hue": 10922, "sat": 254, "bri": 254},  # Yellow
            {"hue": 43690, "sat": 254, "bri": 254},  # Blue
        ]
        celebrate_goal(api, brazil_colors)
    else:
        print(f"Unknown scene: {scene_name}")
        sys.exit(1)

if __name__ == "__main__":
    main()
