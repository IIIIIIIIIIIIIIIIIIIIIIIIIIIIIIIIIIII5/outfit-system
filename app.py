from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/getOutfits/<int:user_id>")
def get_outfits(user_id):
    try:
        response = requests.get(f"https://avatar.roblox.com/v1/users/{user_id}/outfits")
        response.raise_for_status()
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/")
def home():
    return "Roblox Outfit Proxy is online."
