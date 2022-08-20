import requests
from flask import current_app
from api.calls.ms.meta import Meta

class Webhooks:
    def __init__(self, app_host, entities : list, actions = ["CREATE", "UPDATE", "DELETE"]):
        Meta.get_all(entity, filter="action")