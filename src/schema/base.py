# -*- coding: utf-8 -*-

from __future__ import absolute_import


from marshmallow import Schema, fields, post_dump


class BaseResponseSchema(Schema):
    success = fields.Bool(required=True)
    error_message = fields.Str()

    @post_dump
    def remove_empty_fields(self, data):
        return {k: v for k, v in data.items() if v not in (None, {}, '')}
