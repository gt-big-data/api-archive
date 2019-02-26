from flask import Blueprint, request

bp = Blueprint('ping', 'ping', url_prefix='/ping')

@bp.route("/", methods=['GET'])
def ping():
    if request.method == 'GET':
        return "pong"
    else:
        return "405: Restricted method"