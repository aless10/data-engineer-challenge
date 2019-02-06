# -*- coding: utf-8 -*-

from __future__ import absolute_import

from src.model.base import BaseResponse


class TaskRequest:

    def __init__(self, events=None, start_date=None, end_date=None, datetime_range=None, scheduler=None):
        self.events = events
        self.start_date = start_date
        self.end_date = end_date
        self.datetime_range = datetime_range
        self.scheduler = scheduler

    def prepare_task_payload(self):
        return self.__dict__


class TaskResponse(BaseResponse):

    def __init__(self, error_message=None):
        super(TaskResponse, self).__init__(error_message)
        self.publishers_stats = []
        self.top_ten = []
        self.clips_per_country = []

    @classmethod
    def from_scheduler_response(cls, response):
        obj = cls()
        if response['status']:
            obj.response = response["response"]
        else:
            obj.error_message = response['error_message']
        return obj
