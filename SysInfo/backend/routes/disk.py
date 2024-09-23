import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Blueprint, jsonify
from utils.disk_info import get_disk_data

disk_routes = Blueprint('disk', __name__)

@disk_routes.route('/disk')
def disk_info():
    try:
        disk_data = get_disk_data()
        return jsonify(disk_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
