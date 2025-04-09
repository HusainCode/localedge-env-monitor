
# ENS160 Air Quality Sensor Features:
# - eCO2: Equivalent CO₂ level estimation (in ppm), useful for indoor air quality
# - TVOC: Total Volatile Organic Compounds (in ppb), indicates chemical pollutants
# - AQI: Air Quality Index (scale 1–5), gives a general air quality score
# - Status: Sensor health or validity of measurements (e.g., NORMAL, WARMUP)

'''
in	Control digital I/O pins (e.g., turn LEDs on/off, read buttons)
I2C	Communicate with I²C devices like sensors (ENS160, LCDs, etc.)
ADC	Read analog signals (e.g., from potentiometers, light sensors)
PWM	Create pulse-width signals (for dimming LEDs, driving servos, etc.)
'''

from machine  import I2C
import time
import ujson # lighhtwegiht json
import gc # Garbage collection


class ENS160:
    def __init__(self):
        self.air_quality = None
        '''
        eCO₂ (Equivalent Carbon Dioxide) Levels in ppm:
        - 400–1000 ppm     → Good (typical fresh indoor air)
        - 1001–2000 ppm    → Moderate (drowsiness, stale air)
        - 2001–5000 ppm    → Poor (headaches, reduced focus)
        - 5001+ ppm        → Unhealthy (requires ventilation)
         Lower is better. Keep below 1000 ppm for comfort and focus.
        '''
        self.eCO2_level = 0

        '''
        TVOC (Total Volatile Organic Compounds) Levels in ppb:
        - 0–150 ppb     → Good
        - 151–500 ppb   → Moderate
        - 501–1000 ppb  → Poor
        - 1001+ ppb     → Unhealthy
        Lower is better. Aim for under 150 ppb indoors.
        '''
        self.total_TVOC = 0

    @property
    def air_quality(self):
        return self.air_quality

    @air_quality.setter
    def air_quality(self, value):
        self._air_quality = value

    @property
    def eCO2_level(self):
        return self.eCO2_level

    @eCO2_level.setter
    def eCO2_level(self, value):
        self._eCO2_level = value

    def thresholds(self):
        # Normal
        # Warning
        # Critical
        pass

    def data_timestamp(self):
        pass

    def max_min_history(self):
        pass