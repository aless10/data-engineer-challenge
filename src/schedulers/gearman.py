# -*- coding: utf-8 -*-

from __future__ import absolute_import

import logging
import os

from python3_gearman import GearmanClient, PRIORITY_LOW, GearmanWorker
from src.utils.exceptions import SchedulerTimedOut
from src.schedulers.base import Scheduler
from src.utils import json
from src.task.tasks import main_task

log = logging.getLogger()


class GearmanScheduler(Scheduler):

    name = "gearman"
    icon = "images/gearman.jpg"
    tasks = {
        'task': main_task
    }

    def __init__(self, host, port, max_retries=3, poll_timeout=60):
        super(GearmanScheduler, self).__init__()
        server = ":".join([host, str(port)])
        self.connection = GearmanClient([server])
        self.max_retries = max_retries
        self.poll_timeout = poll_timeout
        self.gm_worker = GearmanWorker([server])
        self.create_worker(tasks=self.tasks)

    def close(self):
        self.connection.shutdown()

    def register_task(self, k, v):
        log.info('Register task %s', k)
        return self.gm_worker.register_task(k, v)

    def create_worker(self, tasks=None):

        if tasks is None:
            tasks = dict()

        pid = os.getpid()

        try:

            self.gm_worker.set_client_id(str(pid))

            for k, v in tasks.items():

                self.register_task(k, v)

            self.gm_worker.work()

        except Exception as e:
            log.error("%s -- %s", pid, e)

        finally:
            if self.gm_worker:
                log.info("Shutting down gearman worker")
                self.gm_worker.shutdown()
            else:
                log.error("Cannot shut down gearman worker")

    def schedule(self, task_name, payload):
        response = self.connection.submit_job(
            task_name, json.dumps(payload), background=False, priority=PRIORITY_LOW,
            max_retries=self.max_retries, poll_timeout=self.poll_timeout)
        if response.timed_out:
            raise SchedulerTimedOut('Scheduler request timed out')
        return json.loads(response.result)
