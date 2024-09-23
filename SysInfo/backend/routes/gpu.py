from flask import Blueprint, jsonify
import requests
from utils.gpu_info import get_gpu_info

gpu_routes = Blueprint('gpu', __name__)

@gpu_routes.route('/gpu')
def get_gpu_data():
    try:
        response = requests.get("http://localhost:8085/data.json")
        data = response.json()

        gpu_usage, gpu_temperature = get_gpu_info(data)

        if gpu_usage is None and gpu_temperature is None:
            return jsonify({"error": "Nie znaleziono informacji o GPU"}), 404

        return jsonify({
            "gpu_usage": gpu_usage,
            "gpu_temperature": gpu_temperature
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500
