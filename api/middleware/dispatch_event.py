import functools
from flask import current_app, request, jsonify
from api.middleware.dispatchers.b24_on_task_add import on_task_add

event_dispatchers = {
    "ONTASKADD": on_task_add
}

'''
    Обрабатывает событые в параметре "data"
'''
def dispatch_event(f):
    @functools.wraps(f)
    def decorated(*args, data, **kwargs):
        try:
            event = data['event']
            event_data = data['data']
        except:
            if not current_app.config['PRODUCTION']:
                print("Not an event message passed")

            return jsonify({
                    'error' : 'Ожидается событые (должен содержать поле event и поле data)'
            }), 400
        
        if not event in event_dispatchers:
            return jsonify({
                    'error' : f'Событие {event} не найдено'
            }), 400

        result = event_dispatchers[event](event_data)
        return f(*args, data=result, **kwargs)
    return decorated