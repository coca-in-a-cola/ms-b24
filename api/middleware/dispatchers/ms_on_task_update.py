from api.calls.bitrix24.tasks import Tasks as B24Tasks
from flask import current_app
from api.calls.ms.tasks import Tasks as MSTasks
from api.calls.ms.shared import get_by_meta, get_by_uuid
from api.calls.sync.fetchB24UserFromMeta import fetchB24UserFromMeta
from api.calls.sync.fetchCRMEntityFromMeta import fetchCRMEntityIDFromMeta
from api.calls.sync.findOrCreateFileFromMeta import findOrCreateFileFromMeta
from api.calls.sync.fetchB24TaskFromMeta import fetchB24TaskFromMeta

from munch import Munch, munchify
import re

def on_task_update(meta, **kwargs):
    task = get_by_meta(meta)
    b24_task = fetchB24TaskFromMeta(meta)
    # загружаем файлы в хранилище
    
    B24Tasks().update(id=b24_task.id, data=Munch(
        UF_MS_HREF = meta.href,
        # Будем считать, что заголовок - это первое предложение задачи
        TITLE = re.split(r', |_|-|! |\. ', task.description)[0],
        DESCRIPTION = task.description,
        CREATED_DATE = task.created,
        CHANGED_DATE = task.updated,
        STATUS =  5 if task.done else 1,
        DEADLINE = task.dueToDate if hasattr(task, 'dueToDate') else None,
        CREATED_BY = fetchB24UserFromMeta(task.author.meta).ID,
        RESPONSIBLE_ID = fetchB24UserFromMeta(task.assignee.meta).ID,
        UF_CRM_TASK = [fetchCRMEntityIDFromMeta(task.agent.meta) if hasattr(task, 'agent') else None],
        # UF_WEBDAV_FILES = list(findOrCreateFileFromMeta(task.files.meta)) if hasattr(task, 'files') else None,
        # TODO: привязывать документы к сделкам
    ))
     
