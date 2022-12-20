from flask import Flask, jsonify, request
from data import data

app = Flask (__name__)

@app.route("/")
def index():
    name = request.args.get("name")
    planet_data = next (item for item in data if item["name"==name])
    return jsonify({
        "data":planet_data,
        "message":"success"
    }),200

if __name__ == "__main_":
    app.run()