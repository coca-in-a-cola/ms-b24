from api.calls.ms.shared import get_by_meta
from types import SimpleNamespace
import requests
from flask import current_app
from munch import *

def fetchCRMEntityIDFromMeta(meta):
    entity = get_by_meta(meta)
    
    filter = Munch()

    if hasattr(entity, phone):
        filter.PHONE = entity.phone
    if hasattr(entity, email):
        filter.EMAIL = entity.email

    b24_CRM_entities = {
        "company": "CO",
        "contact": "C",
        "lead": "L"
    }
    
    for entity in ['company', 'contact', 'lead']:
        r = requests.post(
                f"{current_app.config['BITRIX24_INCOMING_WEBHOOK']}crm.{entity}.list",
                json={
                    "FILTER": filter,
                    "SELECT": [
                        'ID'
                    ]
                })

        if r.ok:
            data = munchify(r.json())
            if len(data.result) > 0:
                return f"{b24_CRM_entities[entity]}_{data.result[0].ID}"
    
    return None