from api.calls.ms.shared import get_by_meta, download_by_meta
import requests
from flask import current_app
from munch import *
import base64

def findOrCreateFileFromMeta(meta):
    files = get_by_meta(meta)

    if (files.rows == 0):
        return None
    
    for f in files.rows:
        content = download_by_meta(f.meta)

        r = requests.post(
                f"{current_app.config['BITRIX24_INCOMING_WEBHOOK']}disk.file.uploadversion",
                json={
                    "fileContent": [f.filename, base64.b64encode(content).decode("utf-8")]
                })
        
        if (r.ok):
            response = munchify(r.json())
            yield response.result.ID