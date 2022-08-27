import requests
import urllib.parse
from flask import current_app
from api.schema.ms.meta import MetaDataSchema
from munch import Munch, munchify


def download_by_meta(meta : Munch):
    r = current_app.ms_session.get(meta.downloadHref)
    return r.content

def get_by_meta(meta : Munch):
    r = current_app.ms_session.get(meta.href)
    return munchify(r.json()) if r.ok else None
    

def get_by_uuid(target, uuid):
    r = current_app.ms_session.get(f"{current_app.config['MS_OUTGOING_URI']}/{target}/{uuid}")
    return munchify(r.json()) if r.ok else None


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

        return munchify(json['rows'])


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