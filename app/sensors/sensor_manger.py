#  Purpose:
#
#
#  Key Attributes:
#
#
#  Main Methods:
#
#
#  Example:

class SensorManger:
    def __init__(self, api_key: str, server_url: str):
        self.api_key = api_key
        self.server_url = server_url
        self.dht22_data = {}
        self.esn160_data = {}


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

