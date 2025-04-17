#  Purpose:
#      Loads and controls environment variables used across the application.
#      Provides a centralized configuration interface
#      for secrets, endpoints, and paths.
#
#  Key Attributes:
#      - AWS_ENDPOINT: str –> AWS MQTT broker endpoint
#      - PI_API_URL: str –> Flask server endpoint on Pi5
#      - SECRET_KEY: str –> App-level secret key
#      - DB_PATH: str –> Path to SQLite database file
#
#  Main Methods:
#      - load(): Loads environment variables (supports .env files)
#      - get(attr: str): Fetches a specific configuration value
#

"""
   Sources:
       - https://docs.python.org/3/library/os.html
       - https://pypi.org/project/python-dotenv/
"""
import os
from dotenv import load_dotenv
import sys

class Configuration:
    def __init__(self):
        print("Hello World!")