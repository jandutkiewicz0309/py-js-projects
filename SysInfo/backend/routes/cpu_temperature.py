from flask import Blueprint, jsonify
import requests
from utils.cpu_info import get_cpu_temperature

cpu_temperature_routes = Blueprint('cpu_temperature', __name__)

@cpu_temperature_routes.route('/cpu-temperature')
def get_cpu_temperature_route():
    try:
        response = requests.get("http://localhost:8085/data.json")
        data = response.json()
        temperatures = get_cpu_temperature(data)

        if not temperatures:
            return jsonify({"error": "Nie znaleziono czujników temperatury procesora"}), 404

        return jsonify({"cpu_temperatures": temperatures})

    except Exception as e:
        return jsonify({"error": str(e)}), 500
