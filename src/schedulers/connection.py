# -*- coding: utf-8 -*-

from __future__ import absolute_import


from flask import g

from src.schedulers.celery import CeleryScheduler
from src.schedulers.gearman import GearmanScheduler

SCHEDULERS = {
    'gearman': GearmanScheduler,
    'celery': CeleryScheduler
}


def get_scheduler():
    if 'scheduler' not in g:
        pass
    return g.scheduler


def close_scheduler(e=None):
    scheduler = g.pop('scheduler', None)

    if scheduler is not None:
        scheduler.close()
