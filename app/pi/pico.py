#  Purpose:
#  - Read sensor data from DHT22 and ESN160
#  - Serialize the data into JSON
#  - Send it securely to a Flask server running on Raspberry Pi 5
#
#  Key Attributes:
#  - wifi_ssid: WiFi network name to connect the Pico to
#  - wifi_password: Password for WiFi network
#  - server_url: Flask server endpoint to POST data to
#  - api_key: Simple shared secret for basic security
#
#  Main Methods:
#  - connect_wifi(): Connects Pico to WiFi
#  - read_sensor_data(): Read sensor data
#  - send_data(): Sends JSON payload to server with API Key in header
#
#  Example:
#      pico = Pico()
#      pico.connect_wifi()
#      pico.send_data()

"""
Sources:
   - https://docs.micropython.org/en/latest/library/json.html
   - https://docs.micropython.org/en/latest/library/urequests.html
   - https://docs.micropython.org/en/latest/library/network.WLAN.html
   - https://randomnerdtutorials.com/raspberry-pi-pico-dht11-dht22-micropython/
"""

import urequests
import ujson
import time


class WifiConnectionError(Exception): pass


class PicoError(Exception): pass


import network


class WifiManger:
    UP = True
    DOWN = False
    wifi_ssid = None
    wifi_password = None
    timeout = 10

    def __init__(self):
        self.wlan = network.Wlan(network.STA_IF)  # create wifi connection with station mode
        self.wlan_is_active = wlan.active(self.UP)

    def connect_wifi(self) -> None:
        try:
            self.wlan.connect(self.wifi_ssid, wifi_password)
            while not self.wlan.isconnected() and timeout > 0:
                time.sleep(1)
                timeout -= 1
            if not self.wlan.isconnected():
                pass
        except WifiConnectionError as e:
            raise WifiConnectionError(f"Failed to connect to WiFi!{e}")


import dht
from machine import Pin


class Pico:
    api_key = None
    server_url = None

    def __init__(self, temperature: float, humidity: float, co2: float) -> None:
        self.dht22 = DHT22()
        self.ens160 = ENS160()

        self.temperature = round(self.dht22.temperature, 2)
        self.humidity = round(self.dht23.humidity, 2)
        self.co2 = round(self.ens160.co2, 2)

    def send_dht22_data(self) -> None:
        headers = {
            "Content-Type": "application/json",
            "Authoriztion": f"Bearer {slef.api_key}"
        }
        payload = {
            "temperature": self.temperature,
            "humidity": self.humidity
        }
        try:
            response
            urequests.post(self.server_url, headers=headers, data=usjon.dumps(payload))

        except PicoError as e:
            raise "Falied to send data to the server"
        # I STOPPED HERE

    def send_ens160_data(self):
        pass















