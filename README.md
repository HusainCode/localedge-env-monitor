[![Status](https://img.shields.io/badge/status-in_progress-yellow)]()

# LocalEdge Env Monitor

📅 **GOAL**  
Build a reliable, modular, testable IoT system that reads from **DHT22** and **ENS160** sensors on a **Pico W (MicroPython)** and delivers environmental data to a **Flask API running on a Raspberry Pi 5**. Data is then served to a **Dashboard UI**.

---

## 🔹 Features

- Read temperature & humidity (DHT22)
- Monitor eCO2 and TVOC levels (ENS160)
- Local threshold evaluation on device
- Real-time dashboard served from Pi
- JSON-based communication over HTTP
- SQLite storage and file logger
- AWS MQTT support for remote sync
- Modular, test-driven design


---

## 🩵 Supported Sensors

### ✨ DHT22
- Measures: Temperature (°C), Humidity (%)
- Range: -40 to +80 °C / 0-100% RH
- Resolution: 0.1 °C / 0.1% RH
- Protocol: Single-wire digital

### ✨ ENS160
- Measures: Air Quality Index (AQI), eCO2, TVOC
- Interface: I2C
- Useful for: Indoor air pollution detection

---

## 📚 Key Libraries

### MicroPython (on Pico W)
- `machine`, `time`, `ujson`, `urequests`
- Custom ENS160 MicroPython driver

### Python (on Pi5)
- `flask`, `sqlite3`, `logging`, `requests`, `pytest`, `paho-mqtt`
- `Adafruit_DHT` (if fallback sensor code on Pi is needed)

---

## 🎨 Architecture Diagram

![image](https://github.com/user-attachments/assets/95a894ba-115a-412a-a9ff-460b289d6355)

---

## 🧱 Project Structure

```bash
localedge-env-monitor/
├── app/
│   ├── aws/
│   │   ├── __init__.py
│   │   └── mqtt_client.py        # Publishes to AWS IoT Core
│   ├── pi/
│   │   ├── __init__.py
│   │   └── pi5.py                # Entry point for Flask API on Pi5
│   ├── sensors/
│   │   ├── __init__.py
│   │   ├── dht22.py              # Threshold-aware DHT22 logic
│   │   ├── ens160.py             # Threshold-aware ENS160 logic
│   │   └── sensor_manager.py     # Routes data to storage, logger, cloud
│   ├── storage/
│   │   ├── __init__.py
│   │   └── sqlite_db.py          # SQLite persistence layer
│   ├── app_logging/                     # Centralized app_logging output
│   ├── routes.py                 # Flask endpoints
│   └── __init__.py               # App factory init
├── static/                       # Dashboard static assets
├── templates/
│   └── index.html                # Dashboard frontend
├── test/
│   ├── __init__.py
│   ├── test_dht22.py             # Unit test for DHT22 sensor logic
│   ├── test_ens160.py            # Unit test for ENS160 sensor logic
│   ├── test_sensor_manager.py    # Sensor manager logic test
│   ├── test_flask_api.py         # Flask endpoint + payload format
│   ├── test_logger.py            # Logger formatting / output
│   ├── test_db_storage.py        # SQLite write + read verification
│   └── test_pipeline.py          # E2E integration test
├── README.md                     # You’re here
├── requirements.txt              # Dependencies
├── run.py                        # Main entry for app
├── sandbox.py                    # Dev/test utils
└── .env                          # Secret keys + config (not committed)
```

---

## 🌐 System Overview

- **Pico W (MicroPython)**:
  - Runs sensor code for DHT22 + ENS160
  - Each sensor checks thresholds and returns status
  - Sends data as JSON to Pi via POST `/data`

- **Raspberry Pi 5 (Flask API)**:
  - Receives data from Pico W
  - Sensor Manager stores in SQLite and logs events
  - Dashboard UI fetches real-time values from the API

---

## 🧪 Testing Strategy

| Component           | Test File                  | Description                                  |
| ------------------ | -------------------------- | -------------------------------------------- |
| DHT22 Sensor        | `test/test_dht22.py`        | Unit test for temperature & humidity readings |
| ENS160 Sensor       | `test/test_ens160.py`       | Unit test for AQI, TVOC, and CO₂ thresholds   |
| Sensor Manager      | `test/test_sensor_manager.py` | Validates routing, AWS, and local logging     |
| Flask API           | `test/test_flask_api.py`    | Tests `/data` POST and dashboard GET routes  |
| Logger System       | `test/test_logger.py`       | Verifies log entries, format, and rotation   |
| SQLite Storage      | `test/test_db_storage.py`   | CRUD tests on sensor DB storage layer        |
| End-to-End Pipeline | `test/test_pipeline.py`     | Simulates PicoW → API → SQLite → Dashboard   |
---

## 🚀 Getting Started

### 1. Prepare Pico W

- Flash with MicroPython firmware
- Use `mpremote` to upload MicroPython sensor code

### 2. Set Up Pi5

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python run.py
```

### 3. Connect Sensors

- Connect DHT22 + ENS160 to Pico W GPIO
- Run MicroPython code to send data

### 4. Visit Dashboard

- Access Flask server via browser (e.g. `http://raspberrypi.local:5000`)

---

## 📦 Tech Stack

- 🐍 Python 3.12
- 🌐 Flask
- 🪪 PyTest
- 🛠 SQLite
- 🌬 DHT22, ENS160
- 📶 MicroPython + Pico W

 
