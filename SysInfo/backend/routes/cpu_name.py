from flask import Blueprint, jsonify
import requests
from utils.cpu_info import get_cpu_name

cpu_name_routes = Blueprint('cpu_name', __name__)

@cpu_name_routes.route('/cpu-name')
def get_cpu_name_route():
    try:
        response = requests.get("http://localhost:8085/data.json")
        data = response.json()
        cpu_name = get_cpu_name(data)

        if not cpu_name:
            return jsonify({"error": "Nie znaleziono nazwy procesora"}), 404

        return jsonify({"cpu_name": cpu_name})

    except Exception as e:
        return jsonify({"error": str(e)}), 500
