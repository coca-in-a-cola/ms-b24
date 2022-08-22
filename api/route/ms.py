import os
from flask import Blueprint, jsonify, request, current_app
from api.middleware.dispatch_ms_event import dispatch_events
from api.middleware.fetch_json import fetch_json

ms_api = Blueprint('ms', __name__)

@ms_api.route('/ms', methods=['POST'])
@fetch_json
@dispatch_events
def endpoint(*args, **kwargs):
    return jsonify("OK", 200)

