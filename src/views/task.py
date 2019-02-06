# -*- coding: utf-8 -*-

from __future__ import absolute_import

from flask import render_template
from flask.views import MethodView

from src.schedulers.celery import CeleryScheduler
from src.schedulers.gearman import GearmanScheduler
from src.schema.task import RequestSchema, ResponseSchema
from src.model.task import TaskResponse
from src.task.executor import TaskExecutor


class TaskView(MethodView):

    def get(self):
        return render_template('index.html', schedulers=[CeleryScheduler, GearmanScheduler])

    def post(self):
        executor = TaskExecutor(RequestSchema, ResponseSchema, TaskResponse)
        executor.run()
        return executor.response
