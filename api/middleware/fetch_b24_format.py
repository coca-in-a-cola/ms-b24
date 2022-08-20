import functools
from flask import current_app, request, jsonify
from helpers.parser import parse
from bunch import bunchify

'''
    Обрабатывает запрос из Битрикс24, извлекая из него объект
    В декорируемую функцию передаётся новый параметр data типа dict
'''
def fetch_b24_format(f):
    @functools.wraps(f)
    def decorated(*args, **kwargs):
        try:
            raw = request.get_data(as_text=True)
            
            if not current_app.config['PRODUCTION']:
                print("RAW DATA:\n", raw, '\n-------')

            parsed = parse(raw)
            
            if not current_app.config['PRODUCTION']:
                print("PARSED B24 FORMAT: \n", parsed, '\n-------')
        except:
            if not current_app.config['PRODUCTION']:
                print("FAILED TO PARSE B24 FORMAT")

            return jsonify({
                    'error' : 'Данные неверно закодированы'
            }), 400

        return f(*args, data=bunchify(parsed), **kwargs)
    return decorated