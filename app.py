from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def hello():
    return jsonify({
    "coordinates": {
        "longitude": -79.39560275775827,
        "latitude": 43.66299257717002
    }
})