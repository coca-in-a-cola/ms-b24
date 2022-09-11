from flask import current_app
from api.calls.ms.tasks import Tasks as MSTasks

def on_task_add(data, **kwargs):
    task_id = data['FIELDS_AFTER']['ID']
    task = current_app.B24Tasks.get(task_id)
    if not current_app.config['PRODUCTION']:
        print('Got task by id:\n', task)
    
    #ms_task = MSTasks.add(description = task['title'])
    if not current_app.config['PRODUCTION']:
        print('Posted task:\n', ms_task)
    return ms_task