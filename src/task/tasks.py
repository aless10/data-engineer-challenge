# -*- coding: utf-8 -*-

from __future__ import absolute_import

import click
import logging
from redis import StrictRedis

from src.task.event import create_event
from src.task.utils import time_logged


log = logging.getLogger()
redis_db = StrictRedis()


def add_event_to_queue(date_from, date_to):
    create_event(date_from, date_to, redis_db)


@time_logged
@click.command()
@click.option('--number-of-events',
              required=True, type=int,
              help='Number of fake events to generate')
@click.option('--date-from',
              help='Processing date from, in YYYYMMDD %I:%M:%S format. Leave empty for Now.')
@click.option('--date-to',
              help='Processing date to, in YYYYMMDD %I:%M:%S format. Leave empty for Now.')
def main_task(number_of_events, date_from, date_to):
    log.info("Starting main task")
    for _ in range(number_of_events):
        yield add_event_to_queue(date_from, date_to)
