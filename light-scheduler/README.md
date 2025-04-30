# IoT Light Scheduler

## Objective

The goal of this project is to simulate a real-world IoT dashboard where users can schedule the turning ON and OFF of a light using a graphical interface. The system utilizes network communication to send scheduling commands from the frontend to a backend server, which then forwards the commands to an MQTT broker. A Python MQTT subscriber receives these commands and simulates sending them to an Arduino, turning the light on or off.

---

## Project Structure

- **Frontend**: A browser-based interface using HTML, CSS, and JavaScript that allows users to set the ON and OFF times for scheduling the light in their browser.
- **WebSocket Server**: A Python WebSocket server that listens for schedule updates from the frontend, formats the schedule, and forwards it to an MQTT broker.
- **MQTT Subscriber**: A Python script that subscribes to the MQTT topic, receives the schedule, and simulates sending an "ON" or "OFF" command to the Arduino using a simulated serial connection.

---

## Requirements

- **Python** (version 3.6 or higher)
- **Mosquitto** (for MQTT communication)
  - You can install Mosquitto using the following commands:
    - `sudo apt-get install mosquitto` (Linux)
    - `brew install mosquitto` (macOS)
    - Download from [here](https://mosquitto.org/download/) for Windows.
- **WebSocket Server**: Python WebSocket library
  - Install using: `pip install websockets`
- **MQTT Python client**: Install using: `pip install paho-mqtt`

---

## Setup

1. **Frontend (HTML/CSS/JS)**: 
   - `index.html`: The main interface with input fields for ON and OFF times and a submit button.
   - `Style.css`: Basic styling for the interface.
   - `Script.js`: Handles WebSocket communication with the WebSocket server.

2. **WebSocket Server**:
   - The WebSocket server (`websocket_server.py`) listens for connections from the frontend, receives the schedule (ON and OFF times), and forwards it to the MQTT broker.

3. **MQTT Subscriber**:
   - The MQTT subscriber (`mqtt_subscriber.py`) listens to the MQTT topic (`light/schedule`) and simulates sending commands to the Arduino via a serial interface.

---

## Running the Project

### 1. Start the MQTT Broker

Ensure that your MQTT broker (Mosquitto) is running. You can do this by running the following command:
```bash
mosquitto
