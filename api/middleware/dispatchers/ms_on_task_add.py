from api.calls.bitrix24.tasks import Tasks as B24Tasks
from flask import current_app
from api.calls.ms.tasks import Tasks as MSTasks
from api.calls.ms.shared import get_by_meta, get_by_uuid
from api.calls.sync.fetchB24UserFromMeta import fetchB24UserFromMeta
from munch import Munch, munchify
import re

def on_task_add(meta, **kwargs):
    task = get_by_meta(meta)
    B24Tasks().add(id=task.id, data=dict(
        UF_MS_HREF = meta.href,
        # Будем считать, что заголовок - это первое предложение задачи
        TITLE = re.split(r', |_|-|! |\. ', task.description)[0],
        DESCRIPTION = task.description,
        CREATED_DATE = task.created,
        CHANGED_DATE = task.updated,
        STATUS =  5 if task.done else 1,
        DEADLINE = task.dueToDate if hasattr(task, 'dueToDate') else None,
        CREATED_BY = fetchB24UserFromMeta(task.author.meta).ID,
        RESPONSIBLE_ID = fetchB24UserFromMeta(task.assignee.meta).ID
        #TODO: дописать ещё поля
    ))
    
    print(task)