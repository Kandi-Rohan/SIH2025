import RPi.GPIO as GPIO
import time, random, json
import paho.mqtt.client as mqtt

# MQTT Settings
BROKER = "broker.hivemq.com"
TOPIC = "SIH2025/faults"

# Relay Pin
RELAY_PIN = 17

# Thresholds
vibration_threshold = 500.0
current_threshold = 0.1
temp_threshold = 60.0

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(RELAY_PIN, GPIO.OUT)
GPIO.output(RELAY_PIN, GPIO.HIGH)  # Lamp ON initially

client = mqtt.Client()
client.connect(BROKER, 1883, 60)

def read_sensors():
    # For POC → simulate readings
    vibration = random.uniform(0, 1000)
    current = random.uniform(0, 5)
    temp = random.uniform(20, 100)
    return vibration, current, temp

def detect_fault(vibration, current, temp):
    event, reason = "Normal", "None"
    
    if vibration > vibration_threshold:
        event, reason = "Snap Detected", "Vibration Spike"
        GPIO.output(RELAY_PIN, GPIO.LOW)
    elif current < current_threshold:
        event, reason = "Open Circuit", "Current Drop"
        GPIO.output(RELAY_PIN, GPIO.LOW)
    elif temp > temp_threshold:
        event, reason = "Overheat", "Temperature Rise"
        GPIO.output(RELAY_PIN, GPIO.LOW)
    else:
        GPIO.output(RELAY_PIN, GPIO.HIGH)
    
    return event, reason

def run_node():
    try:
        while True:
            vibration, current, temp = read_sensors()
            event, reason = detect_fault(vibration, current, temp)

            payload = {
                "node_id": "RPI-Node-1",
                "event": event,
                "reason": reason,
                "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S")
            }
            client.publish(TOPIC, json.dumps(payload))
            print("Published:", payload)
            time.sleep(3)
    except KeyboardInterrupt:
        GPIO.cleanup()

if __name__ == "__main__":
    run_node()
