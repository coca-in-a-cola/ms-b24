import functools
from flask import current_app, request, jsonify
from api.middleware.dispatchers.b24_on_task_add import on_task_add
from api.schema.ms.meta import MetaDataSchema

event_dispatchers = {
    'CREATE': on_task_add
}

'''
    Обрабатывает событыя в параметре "data"
'''
def dispatch_events(f):
    @functools.wraps(f)
    def decorated(*args, data, **kwargs):
        result = []
        try:
            events = data['events']
        except:
            return jsonify({
                    'error' : 'Ожидается событые (должен содержать поле events)'
            }), 400
        
        for event in events:
            if not event in event_dispatchers:
                return jsonify({
                        'error' : f'Событие {event} не найдено'
                }), 400

            meta = MetaDataSchema().load(event, partial=True)
            result = result.append(event_dispatchers[event['action']](meta))

        return f(*args, data=result, **kwargs)
    return decorated