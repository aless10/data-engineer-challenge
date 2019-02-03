# -*- coding: utf-8 -*-

from __future__ import absolute_import

from src.schedulers.base import Scheduler


class CeleryScheduler(Scheduler):

    def close(self):
        return

    def schedule(self, task_name, payload):
        return
