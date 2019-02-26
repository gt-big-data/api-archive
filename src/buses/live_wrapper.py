from flask import Blueprint, request, jsonify
from martapy import BusClient
import json

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
