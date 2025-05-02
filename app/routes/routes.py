
# File: app/routes/sensor_routes.py

# Purpose:
#   Define HTTP endpoints related to sensor data (DHT22, ENS160)
#   Route requests to the appropriate sensor manager and DB functions

# Key Attributes:
#   - Uses Flask Blueprint for modular routing
#   - Groups all sensor-related routes under a common URL prefix (/sensor)
#   - Interfaces with sensor_manager to acquire live data
#   - Sends responses as JSON or renders HTML via Jinja2 templates

# Main Methods:
#   - GET /sensor/dht22 → Fetch latest DHT22 readings
#   - GET /sensor/ens160 → Fetch latest ENS160 readings


"""
Flask Blueprint for sensor-related API routes.
"""


from flask import Blueprint, request, jsonify, Response
from sensor_manager.sensor_pipeline import SensorPipeline

main = Blueprint("main", __name__)


@main.route("/")
def home():
    return "LocalEdge is up and running!"

routes = Blueprint("routes", __name__)

pipeline = SensorPipeline(api_key ="124", server_url="https://localhost")


@routes.route("/dht22", methods=["POST"])
def receive_dht22() -> Response:
    raw = request.get_data(as_text=True) # tell Flask the coming data is a text
    data = pipeline.update_dht22_data(raw)
    return jsonify(data)

@routes.route("/ens160", methods=["POST"])
def receive_ens160() -> Response:
    raw = request.get_data(as_text=True)
    data =pipeline.update_ens160_data(raw)
    return jsonify(data)


