from flask import Flask
from flask_cors import CORS
from test import bus_wrapper 

# Make the Flask app and connect the database
app = Flask(__name__)
app.register_blueprint(bus_wrapper)
CORS(app)
