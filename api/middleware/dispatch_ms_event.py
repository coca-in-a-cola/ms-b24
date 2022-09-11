import functools
from flask import current_app, request, jsonify
from api.middleware.dispatchers.ms_on_task_add import on_task_add
from api.middleware.dispatchers.ms_on_task_delete import on_task_delete
from api.middleware.dispatchers.ms_on_task_update import on_task_update

from api.schema.ms.meta import MetaDataSchema
from munch import Munch

event_dispatchers = Munch (
    CREATE = on_task_add,
    UPDATE = on_task_update,
    DELETE = on_task_delete
)

'''
    Обрабатывает событыя в параметре "data"
'''
def dispatch_events(f):
    @functools.wraps(f)
    def decorated(*args, data, **kwargs):
        result = []
        try:
            events = data.events
        except:
            return jsonify({
                    'error' : 'Ожидается событые (должен содержать поле events)'
            }), 400
        
        for event in events:
            if not event.action in event_dispatchers:
                return jsonify({
                        'error' : f'Событие {event.action} не найдено'
                }), 400

            result = result.append(event_dispatchers[event.action](event.meta))

        return f(*args, data=result, **kwargs)
    return decorated