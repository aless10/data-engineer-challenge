# -*- coding: utf-8 -*-

from __future__ import absolute_import

from src.task.event import create_event


async def add_event_to_queue(date_from, date_to, redis_db):
    await create_event(date_from, date_to, redis_db)
