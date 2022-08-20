import requests
from flask import current_app
from api.schema.ms.meta import MetaSchema
import urllib.parse

def get(target: str, window_size = 100, offset = 0, filter:str = None) -> list:
    r = current_app.ms_session.get(
            f"{current_app.config['MS_OUTGOING_URI']}/{target}",
            params = dict(
                filter = urllib.parse.quote_plus(filter),
                limit= {window_size},
                offset = offset,
            ))
    json = r.json()
    return MetaSchema.load(json['rows'], many=True)


class Meta:
    def get_first(target: str, window_size = 100, offset = 0, filter:str = None) -> MetaSchema:
        return get(target, window_size, offset, filter)[0]


    def get_all(target, window_size = 100, filter = None) -> list:
        offset = 0
        result = []
        while(True):
            payload = get(target, window_size, offset, filter)

            if not len(payload):
                break

            result.extend(payload)
            offset += window_size
        return result