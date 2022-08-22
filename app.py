from flask import Flask, jsonify, request
from waitress import serve
from argparse import ArgumentParser
from itertools import chain
from api.route.bitrix24 import bitrix24_api
from api.route.ms import ms_api
import requests
import app_secrets
import app_config

def create_app():
    app = Flask(__name__)
    app.url_map.strict_slashes = False

    # registering blueprints
    # ...
    app.register_blueprint(bitrix24_api)
    app.register_blueprint(ms_api)
    return app


def get_args():
    parser = ArgumentParser()
    parser.add_argument('-t', '--host', default='127.0.0.1', type=str, help='IP-адрес сервера. 0.0.0.0 откроет его для всех публичных адресов, 127.0.0.1 - только на локальном')
    parser.add_argument('-p', '--port', default=8081, type=int, help='Порт, на котором будет работать приложение')
    parser.add_argument('-b', '--production', default=False, action='store_true', help='Отметьте, если сервер работает в боевом режиме')
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    app = create_app()
    args = get_args()
    
    # устанавливаем конфиг
    for key, value in chain(*[[(var, getattr(module, var)) for var in dir(module) \
        if not var.startswith("__")] for module in [app_config, app_secrets, args]]):
        app.config[str(key).upper()] = value
    
    # Открываем сессии и B24 и Мой склад
    ms_session = requests.Session()
    ms_session.auth = (app.config['MS_LOGIN'], app.config['MS_PASSWORD'])
    app.ms_session = ms_session

    port = args.port
    host = args.host

    if (args.production):
        serve(app, host=host, port=port)
    else:
        """
        @app.before_request
        def log_request():
            print("-----")
            print(request.url)
            print(request.headers)
            print(request.data)
            try:
                print(request.json)
            except:
                pass
        """
        app.run(host=host, port=port)
