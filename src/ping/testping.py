from flask import Blueprint
from flask import request

testping = Blueprint('testping', __name__,template_folder='templates')

@testping.route("/ping", methods=['GET'])
def ping():
    if request.method == 'GET':
        return "pong"
    else:
        return "405: Restricted method"