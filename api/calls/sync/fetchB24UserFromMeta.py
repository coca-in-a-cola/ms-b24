from api.calls.ms.shared import get_by_meta
from types import SimpleNamespace
import requests
from flask import current_app

def fetchB24UserFromMeta(meta):
    ms_user = SimpleNamespace(**get_by_meta(meta))
    r = requests.post(
            f"{current_app.config['BITRIX24_INCOMING_WEBHOOK']}user.search",
            json={
                # Пытаемся соспставить по ФИО:
                "FILTER": {
                    "NAME": ms_user.firstName,
                    "LAST_NAME": ms_user.lastName,
                    "SECOND_NAME": ms_user.middleName
                }
            })

    data = r.json()

    if (r.ok and len(data['result'] > 0)):
        # Берём только первого
        b24_user = SimpleNamespace(**data['result'][0])
        return b24_user