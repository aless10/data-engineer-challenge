# -*- coding: utf-8 -*-

from __future__ import absolute_import

from flask import make_response, current_app


DEFAULT_HEADERS = {'Content-Type': 'application/json'}


def custom_error_response(e):
    current_app.logger.warning('unhandled exception %s: %s', e.__class__.__name__, e)
    description = getattr(e, 'description', 'Internal server error')
    code = getattr(e, 'code', 500)
    return make_response(description, code, DEFAULT_HEADERS)
