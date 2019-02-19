# -*- coding: utf-8 -*-


import logging
from flask import request, make_response

from src.schedulers.connection import SCHEDULERS
from src.utils.exceptions import SchedulerTimedOut
from src.views.utils import DEFAULT_HEADERS

log = logging.getLogger()


class TaskExecutor(object):

    def __init__(self, request_schema_class, response_schema_class, response_model_class):
        self.request_schema = request_schema_class(strict=True)
        self.response_schema = response_schema_class()
        self.response_model_class = response_model_class
        self.scheduler = None
        self.response = None

    def run(self):
        request_body = request.form
        request_model, errors = self.request_schema.load(request_body)

        if errors:
            response_model = self.response_model_class.for_failure('Failed Schema Validation', errors)
        else:
            try:
                task_payload = request_model.prepare_task_payload()
                self.scheduler = SCHEDULERS[request_model.scheduler].make()
                scheduler_response = self.scheduler.schedule(task_name="task", payload=task_payload)
                response_model = self.response_model_class.from_scheduler_response(scheduler_response, request_model)
            except SchedulerTimedOut as e:
                response_model = self.response_model_class.for_failure(e)

        response_body = self.response_schema.dumps(response_model)
        self.response = make_response(response_body.data, DEFAULT_HEADERS)
