from flask import Flask
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask.ext.jsonpify import jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hallo Weld!'
