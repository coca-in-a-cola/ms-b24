from api.calls.ms.shared import get_by_meta, download_by_meta
import requests
from flask import current_app
from munch import *
import base64
from datetime import datetime

def findOrCreateFileFromMeta(meta):
    files = get_by_meta(meta)

    if (files.rows == 0):
        return None

    # папка будет называться {uuid задачи в моём складе}
    b24_folder_name = "_".join(meta.href.split('/')[-1])
    b24_folder_id = None

    upload_request = requests.post(
            f"{current_app.config['BITRIX24_INCOMING_WEBHOOK']}disk.folder.getchildren",
            json={
            "id": current_app.config['BITRIX24_ATTACHMENTS_FOLDER_ID'],
            "filter": {"NAME": f"{b24_folder_name}"}})
    
    if (upload_request.ok):
            response = munchify(upload_request.json())
            if len(response.result) < 1:
                b24_folder_request = requests.post(
                    f"{current_app.config['BITRIX24_INCOMING_WEBHOOK']}disk.folder.addsubfolder",
                    json={
                        "id": current_app.config['BITRIX24_ATTACHMENTS_FOLDER_ID'],
                        "data": {"NAME": f"{b24_folder_name}"}})
                
                if not b24_folder_request.ok:
                    return None
                
                b24_folder_id = munchify(b24_folder_request.json()).result.ID

            else:
                b24_folder_id = response.result[0].ID
            


    for file in files.rows:
        file_request = requests.post(
            f"{current_app.config['BITRIX24_INCOMING_WEBHOOK']}disk.folder.getchildren",
            json={
            "id": b24_folder_id,
            "filter": {"NAME": f"{file.filename}"}})
        if not file_request.ok:
            continue

        json = munchify(file_request.json())
        b24_file = json.result[0]
        if (len(json.result) and datetime.fromisoformat(file.created) > b24_file.CREATE_TIME):
            # нужно обновить файл
            content = download_by_meta(file.meta)
            pass
        elif not len(json.result):
            # нужно создать файл
            content = download_by_meta(file.meta)
            upload_request = requests.post(
                    f"{current_app.config['BITRIX24_INCOMING_WEBHOOK']}disk.folder.uploadfile",
                    json={
                        "fileContent": [file.filename, base64.b64encode(content).decode("utf-8")],
                        "rights": {
                        "TASK_ID": 42,
                        "ACCESS_CODE": 'U35' #доступ для пользователя с ID=35, для получения названия типа доступа можно воспользоваться https://dev.1c-bitrix.ru/rest_help/general/access_name.php
                        },

                    })
            if (upload_request.ok):
                response = munchify(upload_request.json())
            yield response.result.ID
        else:
            # файл уже загружен на диск и обновление не требуется
            yield b24_file.ID
        
        
        
