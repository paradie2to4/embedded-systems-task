import paho.mqtt.client as mqtt
import time
import os

# MQTT configuration
MQTT_BROKER = '157.173.101.159'
MQTT_PORT = 1883
MQTT_TOPIC = 'light/schedule'
COMMAND_FILE = 'relay.txt'

# Simulated serial behavior
class MockSerial:
    def write(self, data):
        print(f"Simulated write to Arduino: {data.decode().strip()}")

ser = MockSerial()

def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print("Connected to MQTT broker")
        client.subscribe(MQTT_TOPIC)
    else:
        print(f"Connection failed with code {rc}")

def on_message(client, userdata, msg):
    command = msg.payload.decode().strip()
    print(f"Received MQTT message: {command} at {time.strftime('%H:%M')}")
    with open(COMMAND_FILE, 'w') as f:
        f.write(command)
    if command == '1':
        ser.write(b"ON\n")
    elif command == '0':
        ser.write(b"OFF\n")
    else:
        print(f"Unknown command received: {command}")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_BROKER, MQTT_PORT, 60)

try:
    client.loop_forever()
except KeyboardInterrupt:
    print("Stopping...")
    client.loop_stop()
    client.disconnect()
