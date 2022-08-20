import requests
from flask import current_app
from api.schema.b24.task import TaskSchema
from helpers.caseConverter import camel_case_to_screaming_snake

def get_tasks_fields():
    r = requests.get(f"{current_app.config['BITRIX24_INCOMING_WEBHOOK']}tasks.task.getFields")
    data = r.json()
    return data['result']['fields']


class Tasks:
    def __init__(self) -> None:
        self.fields = get_tasks_fields()
        self.schema = TaskSchema()


    def get(self, id):
        r = requests.post(
            f"{current_app.config['BITRIX24_INCOMING_WEBHOOK']}tasks.task.get",
            json={'taskId':id, 'select': self.fields})
        data = r.json()
        return data['result']['task']
    

    def add(self, id = None, data = {}):
        r = requests.post(
            f"{current_app.config['BITRIX24_INCOMING_WEBHOOK']}tasks.task.add",
            json={'taskId':id, 'fields': data} if id else {'fields': data})
        data = r.json()
        return data