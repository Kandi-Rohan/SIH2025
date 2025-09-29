
import time, random, json
import paho.mqtt.client as mqtt

BROKER = "broker.hivemq.com"
TOPIC = "SIH2025/faults"

client = mqtt.Client()
client.connect(BROKER, 1883, 60)

def simulate():
    events = [
        ("Normal", "None"),
        ("Snap Detected", "Vibration Spike"),
        ("Open Circuit", "Current Drop"),
        ("Overheat", "Temperature Rise")
    ]
    while True:
        event, reason = random.choice(events)
        payload = {
            "node_id": "RPI-Node-1",
            "event": event,
            "reason": reason,
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S")
        }
        client.publish(TOPIC, json.dumps(payload))
        print("Published:", payload)
        time.sleep(3)

if __name__ == "__main__":
    simulate()
