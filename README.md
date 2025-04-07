[![Status](https://img.shields.io/badge/status-in_progress-yellow)]()

# 📱 LocalEdge Env Monitor

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
- `flask`, `sqlite3`, `logging`, `requests`, `pytest`
- `Adafruit_DHT` (if fallback sensor code on Pi is needed)

---
---

## 🎨 Architecture Diagram (WIP)

![Architecture](https://github.com/user-attachments/assets/3231ec72-a0ef-442a-8971-8e4c4e13a851)

---

## 🧱 Project Structure

```bash
localedge-env-monitor/
├── app/
│   ├── pi/
│   │   ├── __init__.py
│   │   └── pi5.py              # Entry point for running the Flask API on Pi5
│   ├── sensors/
│   │   ├── __init__.py
│   │   ├── dht22.py            # Threshold-aware DHT22 sensor logic
│   │   ├── ens160.py           # Threshold-aware ENS160 sensor logic
│   │   └── sensor_manager.py   # Collects validated data, routes to DB and logger
│   ├── routes.py               # Flask endpoints to serve dashboard requests
│   └── __init__.py             # Flask app factory setup
├── static/                     # Static assets for the dashboard (CSS, JS)
├── templates/
│   └── index.html              # Dashboard UI frontend
├── test/
│   ├── __init__.py
│   ├── test_dht22.py           # Unit tests for DHT22 class
│   ├── test_ens160.py          # Unit tests for ENS160 class
│   ├── test_sensor_manager.py  # Unit tests for storage, logging logic
│   ├── test_flask_api.py       # API endpoint behavior and validation
│   └── test_pipeline.py        # End-to-end test from sensors to dashboard
├── README.md                   # You’re here
├── requirements.txt            # Python dependencies
├── run.py                      # Run Flask app
├── sandbox.py                  # Dev scratchpad (experimental/test-only)
└── .env                        # Environment variables (not committed)
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

| Component           | Test File                | Description                           |
| ------------------ | ------------------------ | ------------------------------------- |
| DHT22 Sensor        | `test/test_dht22.py`     | Valid reading logic + thresholds      |
| ENS160 Sensor       | `test/test_ens160.py`    | CO₂, TVOC thresholds + validation     |
| Sensor Manager      | `test_sensor_manager.py` | DB insert, logging, fault isolation   |
| Flask API           | `test_flask_api.py`      | Health checks + endpoint integration  |
| End-to-End Pipeline | `test_pipeline.py`       | Full flow from sensors to dashboard   |
| SQLite Storage      | Inline in sensor_manager | Storage confirmation + exception test |
| Logger Output       | Inline or separate test  | Log file format, timestamp check      |

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

 
