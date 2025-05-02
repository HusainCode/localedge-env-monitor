#  Purpose:
#  - Manage and store parsed sensor data from Pico (DHT22 and ENS160)
#
#  Key Attributes:
#  - api_key: shared secret for validation (if needed)
#  - server_url: optional reference to sender, (Pico)
#  - dht22_data: latest DHT22 reading as text
#  - ens160_data: latest ENS160 reading as text
#
#  Main Methods:
#  - update_dht22_data(raw_txt): parse and store DHT22 data
#  - update_ens160_data(raw_txt): parse and store ENS160 data
#
#  Example:
#      manager = SensorManger(api_key="123", server_url="http://localhost")
#      manager.update_dht22_data("22.5,60,41.2,OK")


class SensorPipeline:
    def __init__(self, api_key: str, server_url: str):
        self.api_key = api_key
        self.server_url = server_url

    def update_dht22_data(self, raw_txt: str) -> dict:
        keys = ["temperature", "humidity", "average", "status"]
        values = raw_txt.split(",")
        self.dht22_data = dict(zip(keys, values))

        return self.dht22_data

    def update_ens160_data(self, raw_txt: str) -> dict:
        keys = ["eCO2 level", "total TVOC", "air quality", "status"]
        values = raw_txt.split(",")
        self.ens160_data = dict(zip(keys,values))

        return self.ens160_data

