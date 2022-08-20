import requests
import urllib.parse
from flask import current_app
from api.schema.ms.meta import MetaDataSchema
from bunch import Bunch, bunchify

def get_by_meta(meta : Bunch):
    r = current_app.ms_session.get(meta.href)
    return bunchify(r.json()) if r.ok else None
    

def get_by_uuid(target, uuid):
    r = current_app.ms_session.get(f"{current_app.config['MS_OUTGOING_URI']}/{target}/{uuid}")
    return bunchify(r.json()) if r.ok else None


def get(target, filter = None, window_size = 100, offset = 0):
        r = current_app.ms_session.get(f"{current_app.config['MS_OUTGOING_URI']}/{target}",
        params = dict(
            limit= {window_size},
            offset = offset,
        ) if filter == None else dict(
            limit= {window_size},
            offset = offset,
            filter =  filter
        ))
        json = r.json()

        if (not "rows" in json or len(json['rows']) == 0):
            return None

        return bunchify(json['rows'])


def get_all(target, filter = None, window_size = 100):
        offset = 0
        result = []
        while(True):
            r = get(target, filter, window_size, offset)
            if not r:
                break
            result.extend(r)
            offset += window_size

        return result


def get_first(target, filter = None):
    r = get(target, filter, window_size=1)
    return r[0] if r else None