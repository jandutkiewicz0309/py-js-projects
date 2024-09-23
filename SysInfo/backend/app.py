from flask import Flask
from flask_cors import CORS
from routes.cpu import cpu_routes
from routes.memory import memory_routes
from routes.motherboard import motherboard_routes
from routes.disk import disk_routes
from routes.cpu_name import cpu_name_routes
from routes.cpu_temperature import cpu_temperature_routes
from routes.gpu import gpu_routes

app = Flask(__name__)
CORS(app)

app.register_blueprint(cpu_routes)
app.register_blueprint(memory_routes)
app.register_blueprint(motherboard_routes)
app.register_blueprint(disk_routes)
app.register_blueprint(cpu_name_routes)
app.register_blueprint(cpu_temperature_routes)
app.register_blueprint(gpu_routes)

if __name__ == '__main__':
    app.run(debug=True, port=5001)


