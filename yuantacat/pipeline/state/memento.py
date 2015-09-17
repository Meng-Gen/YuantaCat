#-*- coding: utf-8 -*-

from yuantacat.common.json_utils import JsonUtils

import logging

class Memento():
    def __init__(self, param):
        self.logger = logging.getLogger(__name__)
        self.json_utils = JsonUtils()
        self.path = param['path']
        self.default_value = param['default_value']
        self.filter_key_list = param['filter_key_list']
        self.value = None

    def load(self):
        self.logger.info('load memento: {0}'.format(self.path))
        try:
            json = self.json_utils.load(self.path)
            self.value = self.json_utils.remove_type(json)
        except IOError as e:
            self.logger.info('cannot find memento file: {0}'.format(self.path))
            self.value = self.default_value 
        except ValueError as e:
            self.logger.info('failed to load memento: {0}'.format(self.path))
            self.value = self.default_value 
        except KeyError as e:
            self.logger.info('failed to build load value: {0}'.format(self.path))
            self.value = self.default_value 
        
    def save(self):
        self.logger.info('save memento: {0}'.format(self.path))
        json = self.json_utils.filter_key_list(self.value, self.filter_key_list)
        json = self.json_utils.add_type(json)
        self.json_utils.save(json, self.path)

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value
