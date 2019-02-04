# -*- coding: utf-8 -*-

from __future__ import absolute_import

from celery import Celery
from src.schedulers.base import Scheduler


class CeleryScheduler(Scheduler):

    name = "celery"
    icon = "images/celery.png"

    def __init__(self, host, port, max_retries, poll_timeout):
        self.connection = Celery()
        self.max_retries = max_retries
        self.poll_timeout = poll_timeout

    def close(self):
        return

    def schedule(self, task_name, payload):
        return
