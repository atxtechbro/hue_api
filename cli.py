import sys

from app.hue_api import HueAPI
from app.scenes import wind_down_scene, work_from_home_scene

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 cli.py <scene_name>")
        sys.exit(1)
    
    scene_name = sys.argv[1]
    api = HueAPI()

    if scene_name == "wind_down_scene":
        wind_down_scene(api)
    elif scene_name == "work_from_home_scene":
        work_from_home_scene(api)
    else:
        print(f"Unknown scene: {scene_name}")
        sys.exit(1)

if __name__ == "__main__":
    main()
