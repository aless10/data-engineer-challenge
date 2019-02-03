# -*- coding: utf-8 -*-

from __future__ import absolute_import


class BaseResponse(object):

    def __init__(self, error_message=None):
        self.error_message = error_message

    @property
    def success(self):
        return not self.error_message

    @classmethod
    def for_failure(cls, error_message):
        return cls(str(error_message))
