import sys
from app.hue_api import HueAPI

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 cli.py <scene_name>")
        sys.exit(1)
    
    scene_name = sys.argv[1]
    api = HueAPI()

    response = api.set_light_state(scene_name)

    print("All lights updated successfully" if response.get('error') is None else response.get('error'))


    # Determine the light_id for the scene you are about to set
    scene_map = {
        'wind_down_scene': 1,  # Assuming light_id 1 for wind_down_scene
        'work_from_home_scene': 2,  # Assuming light_id 2 for work_from_home_scene
    }

    # Fetch and print the current status before applying the new state
    if scene_name in scene_map:
        light_id = scene_map[scene_name]

        light_status_before = api.set_light_state(light_id)
        print(f"Light status before applying {scene_name}:", light_status_before)

    # Set the scene
    if scene_name == "wind_down_scene":
        response = api.set_light_state('wind_down_scene')
    elif scene_name == "work_from_home_scene":
        response = api.set_light_state('work_from_home_scene')
    else:
        print(f"Unknown scene: {scene_name}")
        sys.exit(1)

    # Check and print the response from setting the light state
    if isinstance(response, dict):
        if 'status' in response:
            print(response['status'])
        elif 'error' in response:
            print(f"Error: {response['error']}")
        else:
            print(f"Unexpected response format: {response}")
    else:
        print(f"Unexpected response type: {type(response)}")

    # Fetch and print the current status after applying the new state
    if scene_name in scene_map:
        light_status_after = api.set_light_state(light_id)
        print(f"Light status after applying {scene_name}:", light_status_after)

if __name__ == "__main__":
    main()
