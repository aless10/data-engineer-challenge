# -*- coding: utf-8 -*-

from __future__ import absolute_import

import logging
import random
import time
from contextlib import contextmanager
from datetime import datetime
from functools import wraps

from src.task.countries import countries

log = logging.getLogger()


def generate_id(id_length):
    # log.info("Generating ID of length %s", id_length)
    if id_length == 4:
        new_id = random.randint(1000, 9999)
    elif id_length == 2:
        new_id = random.randint(10, 99)
    else:
        log.error("An error occurs while generating id of length %s", id_length)
        raise Exception
    # log.info("Successfully generated id %s", new_id)
    return new_id


def get_random_country():
    return random.choice(countries)[0]


def generate_random_timestamp(start_date, end_date):
    # log.info("Generating a random timestamp between %s and %s", start_date, end_date)
    return random.randrange(date_conversion(start_date), date_conversion(end_date))


def date_conversion(input_date):
    return time.mktime(time.strptime(" ".join(input_date), "%Y%m%d %H:%M:%S"))


@contextmanager
def perf_timer():
    """
    Log time spent on a block of code. Use it as a context manager.
    with('my_ops'):
        long_ops()
    """
    start_time = datetime.now()
    try:
        yield
    except Exception as e:
        log.error("An exception occurred: %s", e)
    finally:
        end_time = datetime.now()
        log.info(end_time - start_time)


def time_logged(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        with perf_timer():
            return f(*args, **kwargs)

    return wrapper
