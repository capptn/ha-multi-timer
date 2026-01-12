from flask import Flask, request, jsonify, send_from_directory
from scheduler import Scheduler
from ha_client import call_service, get_entities

app = Flask(__name__, static_folder="web")
scheduler = Scheduler(call_service)

@app.route("/")
def ui():
    return send_from_directory("web", "index.html")

@app.route("/api/entities")
def entities():
    return jsonify(get_entities())

@app.route("/api/programs", methods=["GET", "POST"])
def programs():
    if request.method == "POST":
        scheduler.add(request.json)
        return jsonify({"status": "ok"})
    return jsonify(scheduler.list())

app.run(host="0.0.0.0", port=8099)
