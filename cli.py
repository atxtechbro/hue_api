import argparse

from app.hue_api import HueAPI
from app.scenes import romantic_scene, party_scene, stargazing_scene, wind_down_scene, work_from_home_scene, cumbia_light_show

def main():
    parser = argparse.ArgumentParser(description="Control Philips Hue light scenes from the command line.")
    parser.add_argument("scene", choices=["romantic", "party", "stargazing", "wind_down", "work_from_home", "cumbia"], help="The light scene to activate.")
    args = parser.parse_args()

    api = HueAPI()

    if args.scene == "romantic":
        romantic_scene(api)
    elif args.scene == "party":
        party_scene(api)
    elif args.scene == "stargazing":
        stargazing_scene(api)
    elif args.scene == "wind_down":
        wind_down_scene(api)
    elif args.scene == "work_from_home":
        work_from_home_scene(api)
    elif args.scene == "cumbia":
        cumbia_light_show(api)

if __name__ == "__main__":
    main()
