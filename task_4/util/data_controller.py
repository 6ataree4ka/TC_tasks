# -*- coding: utf-8 -*-
import yaml
import os
from .singleton import Singleton


@Singleton
class DataController():

    def __init__(self):
        # Read settings from settings.yaml file
        base_path = os.path.dirname(__file__)
        file_path = os.path.abspath(
            os.path.join(base_path, "..", "settings.yaml"))
        with open(file_path, 'r', encoding='utf-8') as ymlfile:
            self.config = yaml.load(ymlfile)
