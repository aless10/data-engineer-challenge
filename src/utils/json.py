# -*- coding: utf-8 -*-

from __future__ import absolute_import

import datetime
import json


class DatetimeJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (datetime.datetime, datetime.date)):
            return obj.isoformat()
        return super(DatetimeJSONEncoder, self).default(obj)


def dumps(*args, **kwargs):
    return json.dumps(*args, cls=DatetimeJSONEncoder, **kwargs)


def loads(*args, **kwargs):
    return json.loads(*args, **kwargs)
