# -*- coding: utf-8 -*-

from __future__ import absolute_import

import os
from logging.config import fileConfig

from flask import Flask

from src.config.conf import ConfigurationObj
from src.views.task import TaskView
from src.views.utils import custom_error_response


def register_error_handlers(app):
    app.register_error_handler(404, custom_error_response)
    app.register_error_handler(400, custom_error_response)
    app.register_error_handler(500, custom_error_response)


def setup_logging(app):
    fileConfig(app.config["LOG_CONFIG_FILE"], defaults=os.environ)


def create_app():
    app = Flask("DataEngineerChallenge")
    app.config.from_object(ConfigurationObj)
    app.add_url_rule('/', view_func=TaskView.as_view('task-view'))
    app.url_map.strict_slashes = False
    register_error_handlers(app)
    setup_logging(app)
    return app
