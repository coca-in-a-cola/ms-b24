import os
from flask import Blueprint, jsonify, request, current_app
from api.middleware.fetch_b24_format import fetch_b24_format
from api.middleware.dispatch_event import dispatch_event

bitrix24_api = Blueprint('bitrix24', __name__)

@bitrix24_api.route('/bitrix24', methods=['POST'])
@fetch_b24_format
@dispatch_event
def endpoint(*args, **kwargs):
    return jsonify("OK", 200)
