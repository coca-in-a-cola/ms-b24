from api.calls.bitrix24.tasks import Tasks as B24Tasks
from flask import current_app
from api.calls.ms.tasks import Tasks as MSTasks
from api.calls.ms.shared import get_by_meta, get_by_uuid

def on_task_add(meta, **kwargs):
    task = get_by_meta(meta)
    print(task)