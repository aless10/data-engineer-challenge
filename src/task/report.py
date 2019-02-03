# -*- coding: utf-8 -*-

from __future__ import absolute_import

"""
We would like to see a bunch of statistics saved and updated in Redis
- total sum of viewable_time per publisher
- the top 10 publishers by events count
- the number of uniques clips per publisher
- total sum of clips per country viewed by day and by night (day = from 07:00 to 19:00, night = from 19:00 to 07:00)
"""


def publisher_total_viewable_time(publisher_id, viewable_time):
    pass
