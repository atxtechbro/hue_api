import os

from flask import Flask, send_from_directory
from flask_cors import CORS
from hue_api import HueAPI
from scenes import wind_down_scene, work_from_home_scene

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
api = HueAPI()

@app.route('/')
def index():
    return send_from_directory('static/frontend', 'index.html')

@app.route('/wind_down', methods=['GET'])
def wind_down():
    wind_down_scene(api)
    return 'Wind Down Scene Activated', 200

@app.route('/work_from_home', methods=['GET'])
def work_from_home():
    work_from_home_scene(api)
    return 'Work From Home Scene Activated'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
