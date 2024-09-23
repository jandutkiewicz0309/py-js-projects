import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Blueprint, jsonify
from utils.memory_info import get_memory_data

memory_routes = Blueprint('memory', __name__)

@memory_routes.route('/memory')
def memory_info():
    try:
        memory_data = get_memory_data()
        return jsonify(memory_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
