# -*- coding: utf-8 -*-

from __future__ import absolute_import

from python3_gearman import GearmanClient, PRIORITY_LOW
from src.utils.exceptions import SchedulerTimedOut
from src.schedulers.base import Scheduler
from src.utils.json import json


class GearmanScheduler(Scheduler):

    def __init__(self, host, port, max_retries, poll_timeout):
        server = ":".join([host, str(port)])
        self.connection = GearmanClient([server])
        self.max_retries = max_retries
        self.poll_timeout = poll_timeout

    def close(self):
        self.connection.shutdown()

    def schedule(self, task_name, payload):
        response = self.connection.submit_job(
            task_name, json.dumps(payload), background=False, priority=PRIORITY_LOW,
            max_retries=self.max_retries, poll_timeout=self.poll_timeout)
        if response.timed_out:
            raise SchedulerTimedOut('Scheduler request timed out')
        return json.loads(response.result)
