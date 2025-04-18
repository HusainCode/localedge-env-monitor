
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
#   - GET /sensor/dht22   → Fetch latest DHT22 readings
#   - GET /sensor/ens160  → Fetch latest ENS160 readings


"""
Flask Blueprint for sensor-related API routes.
"""


from flask import Blueprint

main = Blueprint("main", __name__)

@main.route("/")
def home():
    return "LocalEdge is up and running!"
