from flask import Flask, render_template, jsonify
import random, time

app = Flask(__name__)

logs = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/data")
def data():
    return jsonify(logs[-10:])  # return last 10 events

# Simulate live events
@app.before_first_request
def simulate():
    import threading
    def loop():
        events = [
            ("Normal", "None"),
            ("Snap Detected", "Vibration Spike"),
            ("Open Circuit", "Current Drop"),
            ("Overheat", "Temperature Rise")
        ]
        while True:
            e, r = random.choice(events)
            logs.append({
                "node_id": "RPI-Node-1",
                "event": e,
                "reason": r,
                "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S")
            })
            time.sleep(5)
    threading.Thread(target=loop, daemon=True).start()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
