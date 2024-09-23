from flask import Blueprint, jsonify
import psutil

cpu_routes = Blueprint('cpu', __name__)

@cpu_routes.route('/cpu')
def get_cpu_data():
    cpu_percent = psutil.cpu_percent(interval=1, percpu=True)
    cpu_freq = psutil.cpu_freq(percpu=True)

    print(f"CPU Percent: {cpu_percent}")
    print(f"CPU Frequency: {cpu_freq}")

    if not isinstance(cpu_freq, list):
        cpu_freq = [cpu_freq] * len(cpu_percent)

    physical_cores = psutil.cpu_count(logical=False)
    logical_cores = psutil.cpu_count(logical=True)

    print(f"Physical cores: {physical_cores}, Logical cores: {logical_cores}")

    logical_cores_data = []
    for i, percent in enumerate(cpu_percent, start=1):
        freq = cpu_freq[i-1].current if cpu_freq and len(cpu_freq) > i-1 and cpu_freq[i-1] else cpu_freq[0].current
        logical_cores_data.append({
            "core": i,
            "usage": percent,
            "frequency": freq
        })

    physical_cores_data = []
    for i in range(physical_cores):
        freq = cpu_freq[i].current if cpu_freq and len(cpu_freq) > i and cpu_freq[i] else cpu_freq[0].current
        physical_cores_data.append({
            "core": i + 1,
            "usage": cpu_percent[i],
            "frequency": freq
        })

    return jsonify({
        "physical_cores": physical_cores_data,
        "logical_cores": logical_cores_data
    })
