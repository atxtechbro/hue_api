from flask import Flask, render_template
from hue_api import HueAPI
from scenes import romantic_scene, party_scene, stargazing_scene

app = Flask(__name__)
api = HueAPI()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/romantic')
def romantic():
    romantic_scene(api)
    return 'Romantic Scene Activated'

@app.route('/party')
def party():
    party_scene(api)
    return 'Party Scene Activated'

@app.route('/stargazing')
def stargazing():
    stargazing_scene(api)
    return 'Stargazing Scene Activated'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
