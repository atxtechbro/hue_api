from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS

from hue_api import HueAPI

app = Flask(__name__, static_folder='static/frontend/build')
CORS(app)  # Enable CORS for all routes

api = HueAPI()

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/lights/<int:light_id>/<action>', methods=['POST'])
def control_light(light_id, action):
    """
    Route to control a specific light's state.

    Parameters:
        light_id (int): ID of the light.
        action (str): 'on' or 'off'.

    Returns:
        JSON response with success or failure message.
    """
    if action not in ["on", "off"]:
        return jsonify({'error': f"Invalid action '{action}'. Use 'on' or 'off'."}), 400
    
    success = api.set_light_state(light_id, action)
    if success:
        return jsonify({'message': f"Light {light_id} turned {action} successfully."}), 200
    else:
        return jsonify({'error': f"Failed to turn {action} light {light_id}."}), 500

if __name__ == '__main__':
    app.run(debug=True)
