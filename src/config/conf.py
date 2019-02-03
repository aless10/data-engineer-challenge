# -*- coding: utf-8 -*-

from __future__ import absolute_import

import configparser
import os


class ConfigurationObj:

    config_parser = configparser.ConfigParser(os.environ)
    app_conf_path = os.environ["CONFIG_PATH"]
    config_parser.read(app_conf_path)

    # Basic Flask Configuration values
    FLASK_ENV = config_parser.get('application', 'env')
    ENV = config_parser.get('application', 'env')
    LOG_CONFIG_FILE = config_parser.get("application", "log_config_file")
