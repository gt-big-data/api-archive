from flask import Blueprint, jsonify
from bson.json_util import dumps

from .db import counties_db

bp = Blueprint('census', 'census', url_prefix='/census')


@bp.route('/')
def get_all():
    return jsonify({
        'fulton-1': fulton_1(),
        'fulton-2': fulton_2(),
        'clayton': clayton(),
        'cobb': cobb(),
        'dekalb': dekalb()
    })


@bp.route('/fulton-1')
def fulton_1():
    return dumps(counties_db['fulton-1'].find_one())


@bp.route('/fulton-2')
def fulton_2():
    return dumps(counties_db['fulton-2'].find_one())


@bp.route('/clayton')
def clayton():
    return dumps(counties_db['clayton'].find_one())


@bp.route('/cobb')
def cobb():
    return dumps(counties_db['cobb'].find_one())


@bp.route('/dekalb')
def dekalb():
    return dumps(counties_db['dekalb'].find_one())


if __name__ == '__main__':
    print(get_all())