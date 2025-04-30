import time
from datetime import datetime
import subprocess
# Schedule map: HH:MM -> MQTT message
schedule = {
    "01:13": "ON",
    "01:17": "OFF"
}
sent_messages = set()
while True:
    now = datetime.now().strftime("%H:%M")
    message = schedule.get(now)
    if message and now not in sent_messages:
        print(f"[{now}] Sending MQTT message: {message}")
        subprocess.run([
            "mosquitto_pub",
            "-h", "82.165.97.169",
            "-t", "relay",
            "-m", message
        ])
        sent_messages.add(now)
    time.sleep(1)