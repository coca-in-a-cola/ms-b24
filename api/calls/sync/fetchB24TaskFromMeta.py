from api.calls.ms.shared import get_by_meta
from types import SimpleNamespace
import requests
from flask import current_app
from munch import *

def fetchB24TaskFromMeta(meta):
    r = requests.post(
            f"{current_app.config['BITRIX24_INCOMING_WEBHOOK']}tasks.task.list",
            json={
                "filter": {
                    "UF_MS_HREF": meta.href,
                },
                "select": ["ID"]
            })

    if not r.ok:
        return None

    data = munchify(r.json())

    if len(data.result.tasks) <= 0:
        return None
        
    return data.result.tasks[0]