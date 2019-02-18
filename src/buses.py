from flask import Blueprint, render_template
from flask import request, jsonify
from martapy import BusClient
import json

bus_wrapper = Blueprint('bus_wrapper', __name__,
                        template_folder='templates')


def get_bus_data(route):
    bus_client = BusClient()
    
    if route is None:
        buses = bus_client.buses()
    else:
        buses = bus_client.buses(route)

    final_list = []

    for b in buses:
        json_dict = {
            'adherence': b.adherence,
            'block_id': b.block_id,
            'block_abbr': b.block_abbr,
            'direction': b.direction,
            'latitude': b.latitude,
            'longitude': b.longitude,
            'msg_time': b.msg_time,
            'route': b.route,
            'stop_id': b.stop_id,
            'timepoint': b.timepoint,
            'trip_id': b.trip_id,
            'vehicle': b.vehicle
        }
        final_list.append(json_dict)
    
    return final_list


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
