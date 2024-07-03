import sys

from app.hue_api import HueAPI
from app.scenes import romantic_scene, party_scene, stargazing_scene, wind_down_scene, work_from_home_scene, chill_soccer_game_night, colombia_goal_celebration, brazil_goal_celebration

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
    elif scene_name == "chill_soccer_game_night":
        chill_soccer_game_night(api)
    elif scene_name == "colombia_goal_celebration":
        colombia_goal_celebration(api)
    elif scene_name == "brazil_goal_celebration":
        brazil_goal_celebration(api)
    else:
        print(f"Unknown scene: {scene_name}")
        sys.exit(1)

if __name__ == "__main__":
    main()
