from flask import Blueprint, jsonify, request

from .live_wrapper import get_bus_data
from .marta_gtfs import get_predicted_position

bp = Blueprint('buses', 'buses', url_prefix='/buses')


@bp.route("/live", methods=['GET'])
def get_buses():
    if request.method == 'GET':
        return jsonify(get_bus_data(None))  # Transforms data stored
    else:
        return "405: Restricted method"


@bp.route("/live/<int:route>", methods=['GET'])
def get_buses_by_route(route):
    if request.method == 'GET':
        return jsonify(get_bus_data(route))  # Transforms data stored
    else:
        return "405: Restricted method"


@bp.route("/predicted", methods=['GET'])
def get_predicted_buses():
    return jsonify(get_predicted_position(None))


@bp.route("/predicted/<int:route>", methods=['GET'])
def get_predicted_buses_by_route(route):
    return jsonify(get_predicted_position(route))
