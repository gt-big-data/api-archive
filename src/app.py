from flask import Flask
from flask_cors import CORS
from flask import request
from marta.buses.marta_bus_wrapper import bus_wrapper
from ping.testping import testping

# Make the Flask app and connect the database
app = Flask(__name__)
app.register_blueprint(bus_wrapper)
app.register_blueprint(testping)
CORS(app)

@app.route("/aman",methods=['GET'])
def aman():
    if request.method == 'GET' :
        return "hello"
    else:
        return "goodbye"
