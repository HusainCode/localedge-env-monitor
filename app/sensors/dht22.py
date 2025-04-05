import os
# import adafruit_dht
import board
import time


class MockDHT:
    def __init__(self):
        # fahrenheit = (Celsius * 9/5) + 32
        # Temperature
        # Range: -40°C to +80°C
        # Accuracy: ±0.5°C
        # Resolution: 0.1°C
        self.temperature = 14

        # Humidity
        # Range: 0 % to
        # 100 % RH
        # Accuracy: ±2–5 % RH
        # Resolution: 0.1 % RH
        self.humidity = 33
        self.average_reading = None

    # Check to see if the sensor is reading data
    def is_reading(self):
        pass

    def thresholds(self):
        # Normal
        # Warning
        # Critical
        pass

    @property
    def average_readings(self):
        return self.average_readings

    @property
    def read_temperature(self):
        return self.temperature

    @property
    def read_humidity(self):
        return self.humidity



dhtDevice = MockDHT()

# I STOPPED HERE
# DESIGN THE ARCHITECTURE