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
    def __init__(self, env_path=".env"):
        self.env_path = env_path
        self._loaded = False
        self.load()

    def load(self):
        """
        Loads environment variables from a .env file or system environment.
        """
        load_dotenv(dotenv_path=self.env_path)
        self.AWS_ENDPOINT = os.getenv("AWS_ENDPOINT")
        self.PI_API_URL = os.getenv("PI_API_URL")
        self.SECRET_KEY = os.getenv("SECRET_KEY")
        self.DB_PATH = os.getenv("DB_PATH")
        self._loaded = True

    def get(self, attr: str):
        """
        Fetch a specific configuration value using attribute name.
        """
        if not self._loaded:
            raise RuntimeError("Environment variables not loaded.")
        return getattr(self, attr, None)