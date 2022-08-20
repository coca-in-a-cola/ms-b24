import requests
from flask import current_app
from api.calls.ms.shared import get_all
from api.schema.ms.task import TaskSchema

class Tasks:
    def get_all(self, window_size = 100):
        return get_all(target="entity/task")
    
    def add(**kwargs):
        schema = TaskSchema().dump(**kwargs)
        r = current_app.ms_session.post('https://online.moysklad.ru/api/remap/1.2/entity/task', json=schema)
        return r.json()