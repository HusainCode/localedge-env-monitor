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
"""
# ==============================================================================
# Useful Functions for Interacting with SQLite and AWS
# ==============================================================================
# SQLite Interaction (Local Database):
# ------------------------------------
# 1. connect_to_db(path)         - Establish a connection to a local .db file.
# 2. execute(query, params)      - Run INSERT, UPDATE, DELETE, or schema changes.
# 3. fetchone(query, params)     - Get a single row from SELECT.
# 4. fetchall(query, params)     - Get all rows from SELECT.
# 5. executemany(query, list)    - Efficient batch inserts/updates.
# 6. backup_db(dest_path)        - Copy the SQLite file (for upload or sync).
# 7. close_connection()          - Cleanly close DB connection (if not using context manager).

# AWS Interaction (S3, RDS, etc.):
# --------------------------------
# 8. upload_to_s3(bucket, key, file_path)        - Push local DB or file to AWS S3.
# 9. download_from_s3(bucket, key, dest_path)    - Pull SQLite DB or any file from S3.
# 10. connect_to_rds(host, user, pass, db)       - (If using AWS RDS) Connect to hosted SQL DB.
# ==============================================================================
# Sources:
#   - SQLite:
#       - https://docs.python.org/3/library/sqlite3.html
#       - https://sqlite.org/docs.html
#
#   - AWS SDKs & Services:
#       - https://boto3.amazonaws.com/v1/documentation/api/latest/index.html
#       - https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html
#       - https://docs.aws.amazon.com/iot/latest/developerguide/mqtt.html
#       - https://github.com/aws/aws-iot-device-sdk-python-v2
#
#   - MQTT:
#       - https://pypi.org/project/paho-mqtt/
#
#   - SQL Clients:
#       - https://www.psycopg.org/docs/
#       - https://pymysql.readthedocs.io/
"""

import paho.mqtt.client as mqtt
import ssl
import boto3

class MqttClient:
    def __init__(self, client_id, endpoint, port, cert_path, key_path, ca_path, topic):
        self.s3 = boto3.resource("s3") # s3 object manager




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

