 SIH 2025 – Developing a cost effective solution for detecting the breakage of Low Voltage AC Distribution Over Head conductors
 
🔎 Problem Statement

Overhead low-voltage AC distribution conductors often break due to storms, aging, or accidents, leading to:

Power outages

Electrocution hazards from live wires on the ground

Delays in maintenance because faults are reported late


💡 Proposed Solution

We propose a cost-effective IoT + AI system with pole-mounted nodes that detect conductor faults using:

Vibration, current, and temperature sensors

Raspberry Pi for processing + relay control

MQTT-based fault reporting

When a fault is detected:

The node isolates the load (lamp/fan) using a relay

Publishes a real-time fault alert to a central dashboard

Faults can be verified by peer nodes or crowd-sourced reports for higher reliability


🎯 Proof of Concept (POC)

Since final deployment hardware is unavailable, the POC uses Raspberry Pi with simulated sensor values.

Node (Python script):

Simulates vibration, current, and temperature readings

Detects faults based on thresholds

Controls relay (turns OFF lamp if fault occurs)

Publishes event JSON to MQTT broker (broker.hivemq.com)

Dashboard (Subscriber script):

Subscribes to MQTT topic (SIH2025/faults)

Displays live fault events

Demo Flow:

Lamp ON initially

Simulated fault triggers → Lamp OFF

Dashboard shows fault reason + timestamp


🛠 Hardware (POC Setup)

Raspberry Pi (any model with Wi-Fi + GPIO)

Relay module (to control demo lamp/LED bulb)

Lamp/LED bulb as demo load

Breadboard + jumper wires

(Real deployment will use ADXL345 accelerometer, ACS712 current sensor, DS18B20 temperature sensor, and waterproof casing.)


🧪 Testing Scenarios

-> Wind swing → No alert

-> Simulated snap (vibration spike) → Lamp OFF + alert

-> Open circuit (low current) → Fault alert

-> Overheat simulation (high temp) → Fault alert


🧑‍🤝‍🧑 Team Roles (6 Members)

2 – K.V.ROhith Sai & Mokshagna [Hardware & wiring (Raspberry Pi + relay)]

1 – Abhijna [Firmware (sensor logic + MQTT on Raspberry Pi)]

1 – Ritesh [ML (TinyML model, future extension)]

1 – Rohan [Dashboard/backend (subscriber, Grafana integration)]

1 – Sujay [App & presentation (crowd reporting + demo prep)]


▶️ How to Run POC
1. On Raspberry Pi (Node)
python3 node.py


Publishes simulated events every 3 seconds.

2. On Laptop/Raspberry Pi (Subscriber/Dashboard)
python3 dashboard.py


Shows live alerts:

Node: RPI-Node-1 | Event: Snap Detected | Reason: Vibration Spike | Time: 2025-09-29T22:15:00


🌍 Impact

This system reduces:

-> Electrocution accidents

-> Fault detection time (minutes vs hours)

-> Maintenance costs for utilities

Scalable nationwide via LoRaWAN / 4G / cloud dashboard.
