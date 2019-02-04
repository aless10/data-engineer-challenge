# -*- coding: utf-8 -*-

from __future__ import absolute_import


import abc


class Scheduler(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def close(self):
        return

    @abc.abstractmethod
    def schedule(self, task_name, payload):
        return
