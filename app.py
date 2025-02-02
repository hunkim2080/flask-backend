from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime, timedelta

app = Flask(__name__)
CORS(app)  # CORS 허용 (프론트엔드에서 API 사용 가능)

feeding_logs = []

@app.route("/log", methods=["POST"])
def log_feeding():
    data = request.json
    baby = data.get("baby")
    milk = data.get("milk")
    interval = data.get("interval")

    if not baby or not milk or not interval:
        return jsonify({"error": "Missing data"}), 400

    now = datetime.now().strftime("%H:%M")
    next_time = (datetime.now() + timedelta(hours=interval)).strftime("%H:%M")

    log_entry = {"baby": baby, "milk": milk, "start_time": now, "next_time": next_time}
    feeding_logs.append(log_entry)

    return jsonify(feeding_logs), 200

@app.route("/logs", methods=["GET"])
def get_logs():
    return jsonify(feeding_logs), 200

if __name__ == "__main__":
    app.run(debug=True)