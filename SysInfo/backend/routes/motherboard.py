import sys
import os
import requests 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Blueprint, jsonify
from utils.motherboard_info import find_motherboard_name

motherboard_routes = Blueprint('motherboard', __name__)

@motherboard_routes.route('/motherboard-name')
def get_motherboard_name():
    try:
        response = requests.get("http://localhost:8085/data.json")
        data = response.json()
        motherboard_name = find_motherboard_name(data)

        if not motherboard_name:
            return jsonify({"error": "Nie znaleziono nazwy płyty głównej"}), 404

        return jsonify({"motherboard_name": motherboard_name})

    except Exception as e:
        return jsonify({"error": str(e)}), 500
