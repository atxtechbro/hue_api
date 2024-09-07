from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS

from hue_api import HueAPI

app = Flask(__name__, static_folder='static/frontend/build')
CORS(app)  # Enable CORS for all routes

api = HueAPI()

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/wind_down')
def wind_down():
    api.set_light_state('wind_down_scene')
    return 'Wind Down Scene Activated', 200

@app.route('/work_from_home')
def work_from_home():
    api.set_light_state('work_from_home_scene')
    return 'Work From Home Scene Activated', 200

@app.route('/circadian_lighting', methods=['POST'])
def circadian_lighting():
    response = api.set_circadian_lighting()
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)  # For production, use app.run(host='0.0.0.0', port=5000) or similar configuration
