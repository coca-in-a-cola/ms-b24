from flask import current_app
from api.calls.ms.tasks import Tasks as MSTasks
from api.calls.ms.shared import get_by_meta, get_by_uuid
from api.calls.sync.fetchB24UserFromMeta import fetchB24UserFromMeta
from api.calls.sync.fetchCRMEntityFromMeta import fetchCRMEntityIDFromMeta
from api.calls.sync.findOrCreateFileFromMeta import findOrCreateFileFromMeta
from api.calls.sync.fetchB24TaskFromMeta import fetchB24TaskFromMeta

from munch import Munch, munchify
import re

def on_task_delete(meta, **kwargs):
    b24_task = fetchB24TaskFromMeta(meta)
    # загружаем файлы в хранилище
    
    current_app.B24Tasks.delete(id=b24_task.id)
     
