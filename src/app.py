from flask import Flask, request, jsonify
from datetime import datetime, timedelta
from flask_sqlalchemy import SQLAlchemy
from martapy import BusClient
import os
from flask_cors import CORS

# Make the Flask app and connect the database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] \
        = 'sqlite:///' + os.path.join(os.getcwd(), "buses.db")
CORS(app)
db = SQLAlchemy(app)


def get_db_data(route):
    """
    Retrieves all the Bus data from the database and returns it in JSON format
    """

    # Queries for Bus objects, depending on if route is passed to get_db_data()
    if route is None:
        buses = Bus.query.all()
    else:
        buses = Bus.query.filter_by(route=route)


    final_list = []

    # Parses through every Bus in buses, turns the necessary data into a
    # dictionary, and adds every dictionary to final_list
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


class Bus(db.Model):
    """ Class representing a Bus from the MARTA API and all its attributes """

    id = db.Column(db.Integer, primary_key=True)
    adherence = db.Column(db.String(10), nullable=False)
    block_id = db.Column(db.String(10), nullable=False)
    block_abbr = db.Column(db.String(10), nullable=False)
    direction = db.Column(db.String(25), nullable=False)
    latitude = db.Column(db.String(25), nullable=False)
    longitude = db.Column(db.String(25), nullable=False)
    msg_time = db.Column(db.String(30), nullable=False)
    route = db.Column(db.String(10), nullable=False)
    stop_id = db.Column(db.String(20), nullable=False)
    timepoint = db.Column(db.String(120), nullable=False)
    trip_id = db.Column(db.String(20), nullable=False)
    vehicle = db.Column(db.String(20), nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return '<ID %r>' % self.id


def get_bus_data(route):
    '''
    Method that determines if a new call to the MARTA API should be done.
    Returns a call to get_db_data()
    '''

    # Makes sure the database has been created for Buses in case the file
    # gets deleted
    db.create_all()

    # Determines if the database is empty or if the first entry was added
    # more than 5 minutes before
    if (len(Bus.query.all()) == 0
        or datetime.now() > (Bus.query.all()[0].updated_at
                              + timedelta(minutes = 5))):


        #  Clears the current database
        db.session.query(Bus).delete()
        db.session.commit()

        # Calls the MARTA API
        bus_client = BusClient()
        buses = bus_client.buses()
        db.create_all()

        # Parses through the JSON for each bus and adds it to the database
        for b in buses:
            db.session.add(Bus(
                adherence = b.adherence,
                block_id = b.block_id,
                block_abbr = b.block_abbr,
                direction = b.direction,
                latitude = b.latitude,
                longitude = b.longitude,
                msg_time = b.msg_time,
                route = b.route,
                stop_id = b.stop_id,
                timepoint = b.timepoint,
                trip_id = b.trip_id,
                vehicle = b.vehicle,
            ))
        db.session.commit()

    return get_db_data(route)


@app.route("/get_buses", methods=['GET'])
def get_buses():
    if request.method == 'GET':
        return jsonify(get_bus_data(None)) #Transforms data stored
    else:
        return "405: Restricted method"


@app.route("/get_buses/<int:route>", methods=['GET'])
def get_buses_by_route(route):
    if request.method == 'GET':
        return jsonify(get_bus_data(route)) #Transforms data stored
    else:
        return "405: Restricted method"