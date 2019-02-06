# -*- coding: utf-8 -*-

from __future__ import absolute_import


import abc
import configparser
import os


class Scheduler(abc.ABCMeta):

    name = None

    def __init__(self, *args, **kwargs):
        pass

    @classmethod
    def make(cls):
        config_parser = configparser.ConfigParser(os.environ)
        config_parser.read(os.environ["SCHEDULER_CONFIG_PATH"])
        host = config_parser.get(cls.name, "host")
        port = config_parser.get(cls.name, "port")
        return cls(host, port)

    @abc.abstractmethod
    def close(self):
        return

    @abc.abstractmethod
    def schedule(self, task_name, payload):
        return
