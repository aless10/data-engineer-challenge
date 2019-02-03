# -*- coding: utf-8 -*-

from __future__ import absolute_import

from flask import render_template
from flask.views import MethodView

from src.schema.task import RequestSchema, ResponseSchema
from src.model.task import TaskRequest
from src.task.executor import TaskExecutor


class TaskView(MethodView):

    def get(self):
        return render_template('index.html')

    def post(self):
        executor = TaskExecutor(RequestSchema, ResponseSchema, TaskRequest)
        executor.run()
        return executor.response
