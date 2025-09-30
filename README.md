**SIH 2025 – Developing a cost effective solution for detecting the breakage of Low Voltage AC Distribution Over Head conductors**
==========================================================================================================================================

**Problem Statement**
------------------------------------------------------------------------------------------------------------------------------------------
Overhead low-voltage AC distribution conductors are prone to breakage due to storms, aging infrastructure, or accidental impact. This results in:

- Power outages affecting large areas

- Electrocution hazards from live conductors falling to the ground

- Delays in maintenance due to late fault reporting

**Proposed Solution**

We propose a cost-effective IoT and AI-based system with pole-mounted nodes to detect conductor faults in real-time. The system uses:

- Vibration, current, and temperature sensors

- Raspberry Pi for edge processing and relay-based isolation

- MQTT protocol for fault reporting to a central dashboard

**Key Features**
------------------------------------------------------------------------------------------------------------------------------------------

**Fault Detection:** Identifies abnormal vibrations, sudden current drops, or overheating.

**Isolation:** Disconnects the load (lamp/LED in POC) via a relay when a fault is detected.

**Alerting:** Publishes structured JSON events to an MQTT broker for monitoring.

**Verification:** Faults can be cross-checked with neighboring nodes or user crowd-sourced reports.

**Proof of Concept (POC)**
------------------------------------------------------------------------------------------------------------------------------------------
Since deployment hardware is unavailable, the POC uses Raspberry Pi with simulated sensor values.

**Node (Python script):**

- Generates simulated vibration, current, and temperature readings

- Detects faults using predefined thresholds

- Controls relay (turns OFF lamp/LED when fault occurs)

- Publishes event JSON messages to MQTT broker (broker.hivemq.com)

**Dashboard (Python subscriber):**

- Subscribes to MQTT topic (SIH2025/faults)

- Displays real-time fault events with node ID, reason, and timestamp

**Demo Flow**

- Lamp/LED is ON initially

- Simulated fault (snap/overheat/open circuit) → Relay OFF → Lamp/LED switches OFF

- Dashboard displays fault details with timestamp

**Hardware (POC Setup)**

- Raspberry Pi (any model with Wi-Fi + GPIO)

- Relay module for switching demo lamp/LED bulb

- Lamp/LED bulb as the test load

- Breadboard and jumper wires

- Future deployment will replace simulated values with actual sensor modules:

- ADXL345 accelerometer (vibration monitoring)

- ACS712 current sensor (current monitoring)

- DS18B20 digital temperature sensor (temperature monitoring)

- Waterproof casing for field deployment

**Testing Scenarios**
------------------------------------------------------------------------------------------------------------------------------------------

Normal condition (wind swing): No alert

Conductor snap (vibration spike): Relay OFF + fault alert

Open circuit (low current): Fault alert

Overheating (temperature rise): Fault alert

**Team Roles (6 Members)**
------------------------------------------------------------------------------------------------------------------------------------------

K.V. Rohith Sai & Mokshagna – Hardware setup and wiring (Raspberry Pi + relay)

Abhijna – Firmware development (sensor simulation + MQTT client)

Ritesh – Machine Learning module (TinyML for predictive fault detection, future extension)

Rohan – Backend/Dashboard (subscriber, data visualization, Grafana integration)

Sujay – Mobile app & presentation (crowd reporting and demo preparation)

**How to Run the POC**
------------------------------------------------------------------------------------------------------------------------------------------

On Raspberry Pi (Node):

python3 node.py


→ Publishes simulated sensor events every 3 seconds

On Laptop/Raspberry Pi (Dashboard):

python3 dashboard.py


→ Displays fault alerts in real time, e.g.:

Node: RPI-Node-1 | Event: Snap Detected | Reason: Vibration Spike | Time: 2025-09-29T22:15:00

**Impact**
------------------------------------------------------------------------------------------------------------------------------------------

**The proposed system reduces:**

Risk of electrocution accidents

Fault detection time (minutes instead of hours)

Maintenance and repair costs for utilities

It is scalable nationwide using LoRaWAN, 4G, or cloud-based dashboards.
