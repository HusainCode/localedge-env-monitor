"""
Sources:
   - https://docs.aws.amazon.com/iot/latest/developerguide/mqtt.html
   - https://pypi.org/project/paho-mqtt/
   - https://github.com/aws/aws-iot-device-sdk-python-v2
"""

import paho.mqtt.client as mqtt
import ssl
import boto3

class MqttClient:
    def __init__(self, client_id, endpoint, port, cert_path, key_path, ca_path, topic):
        self.client_id = client_id
        self.endpoint = endpoint # example: a1b2c3d4e5f6g7-ats.iot.us-west-2.amazonaws.com
        self.port = port # stander port for MQTT 8883
        self.cert_path = cert_path
        self.key_path = key_path
        self.ca_path = ca_path
        self.topic = topic

        self.client = mqtt.Client(client_id=self.client_id)
        self.client.tls_set(ca_certs=self.ca_path,
                            certfile=self.cert_path,
                            keyfile=self.key_path,
                            tls_version=ssl.PROTOCOL_TLSv1_2)

    def connect(self):
        self.client.connect(self.endpoint, self.port)
        self.client.loop_start()
        print("Connected to AWS IoT")

    def publish(self, message):
        self.client.publish(self.topic, message)
        print(f"Published: {message}")

    def disconnect(self):
        self.client.loop_stop()
        self.client.disconnect()
        print("Disconnected")

