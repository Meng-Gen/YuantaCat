#-*- coding: utf-8 -*-

from yuantacat.common.json_utils import JsonUtils
from yuantacat.common.file_utils import FileUtils
from yuantacat.report.data_merger import DataMerger

class DataCreator():
    def __init__(self):
        self.json_utils = JsonUtils()
        self.file_utils = FileUtils()
        self.data_merger = DataMerger()

    def create(self, param):
        json = self.__build_json(param)
        path = self.__build_path(param)
        self.__save(json, path)

    def __build_json(self, param):
        return self.data_merger.merge(param)

    def __build_path(self, param):
        if 'path' in param:
            return param['path']
        else:
            relative_path = '''{key}.json'''.format(key=param['stock_symbol'])
            return self.file_utils.join_paths(param['base_path'], relative_path)

    def __save(self, json, path):
        self.json_utils.save(json, path)
        