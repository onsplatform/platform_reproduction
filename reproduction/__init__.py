import logging

from flask import Flask

from reproduction.settings import *
from reproduction.api import construct_blueprint
from platform_sdk.process_memory import ProcessMemoryApi


def create_app(test_config=None):
    """
    Application Factory. Register new modules below.
    :param test_config:
    :return:
    """

    app = Flask(__name__, instance_relative_config=True)
    app.config["JSON_SORT_KEYS"] = False
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)

    @app.route('/')
    def hello():
        return 'Hello, World! The application is running.'

    app.register_blueprint(construct_blueprint(ProcessMemoryApi(PROCESS_MEMORY)))

    return app
