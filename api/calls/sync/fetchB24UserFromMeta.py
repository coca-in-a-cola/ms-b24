from api.calls.ms.shared import get_by_meta
from types import SimpleNamespace
import requests
from flask import current_app
from munch import *

def fetchB24UserFromMeta(meta):
    ms_user = get_by_meta(meta)
    r = requests.post(
            f"{current_app.config['BITRIX24_INCOMING_WEBHOOK']}user.search",
            json={
                # Пытаемся соспставить по ФИО:
                "FILTER": {
                    "NAME": ms_user.firstName,
                    "LAST_NAME": ms_user.lastName,
                    "SECOND_NAME": ms_user.middleName if hasattr(ms_user, 'middleName') else ""
                }
            })

    if not r.ok:
        return None

    data = munchify(r.json())

    if len(data['result']) < 0:
        return None
        
    b24_user = data.result[0]
    return b24_user