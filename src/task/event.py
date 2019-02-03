# -*- coding: utf-8 -*-

from __future__ import absolute_import

import logging
import random
import uuid
from src.task.utils import generate_id, get_random_country, generate_random_timestamp

log = logging.getLogger()


def create_event(start_date, end_date, redis_db):
    # log.info("Creating event with start_date %s and end_date %s", start_date, end_date)
    event = {'clip': generate_id(4),
             'country': get_random_country(),
             'event_id': uuid.uuid4().hex,
             'publisher_id': generate_id(2),
             'viewable_time': random.randint(1, 30),
             'timestamp': generate_random_timestamp(start_date, end_date)
             }
    # log.info("Event ID %s created", event["event_id"])
    redis_db.set(event['event_id'], event)

# Where:
#  - clip is an id of 4 random numbers
#  - country is the country code
#  - event_id is an uuid of the event
#  - publisher_id is an id of 2 random numbers
#  - viewable_time is the time in seconds of the ad viewed (max 30)
#  - timestamp is the unix timestamp of the event
