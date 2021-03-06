#! /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
__author__ = 'Heng Xin'
__date__ = '2018/8/11'
"""

from utils.Log import Log
import yaml
import os

# env = "DEBUG"


class Config(object):
    L = Log('Config')

    def __init__(self, name):
        self.name = name
        current_path = os.path.dirname(os.path.abspath(__file__))
        settings = yaml.load(open(current_path + "/" + name + ".yaml", encoding='utf-8'))
        self.data = settings
        # data = settings[env]
        # self.L.logger.debug(self.data)
