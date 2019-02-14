from flask import Blueprint, render_template
from flask import request, jsonify
from martapy import BusClient

bus_wrapper = Blueprint('bus_wrapper', __name__,
                        template_folder='templates')


def get_bus_data(route):
    bus_client = BusClient()
    buses = bus_client.buses()

    return buses


@bus_wrapper.route("/get_buses", methods=['GET'])
def get_buses():
    if request.method == 'GET':
        return jsonify(get_bus_data(None)) #Transforms data stored
    else:
        return "405: Restricted method"


@bus_wrapper.route("/get_buses/<int:route>", methods=['GET'])
def get_buses_by_route(route):
    if request.method == 'GET':
        return jsonify(get_bus_data(route)) #Transforms data stored
    else:
        return "405: Restricted method"
