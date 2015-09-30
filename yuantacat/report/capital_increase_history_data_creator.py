#-*- coding: utf-8 -*-

from yuantacat.analyzer.capital_increase_history_analyzer import CapitalIncreaseHistoryAnalyzer
from yuantacat.common.json_utils import JsonUtils
from yuantacat.common.file_utils import FileUtils
from yuantacat.report.data_merger import DataMerger

class CapitalIncreaseHistoryDataCreator():
    def __init__(self):
        self.json_utils = JsonUtils()
        self.file_utils = FileUtils()
        self.data_merger = DataMerger()
        self.base_path = './yuantacat/data/report/capital_increase_history/'

    def create(self, param):
        stock_symbol = param['stock_symbol']
        analyzer = CapitalIncreaseHistoryAnalyzer(stock_symbol)
        capital_increase_by_cash = analyzer.get_capital_increase_by_cash().get()
        capital_increase_by_earnings = analyzer.get_capital_increase_by_earnings().get()
        capital_increase_by_surplus = analyzer.get_capital_increase_by_surplus().get()
        json = self.data_merger.merge({
            'data' : {
                'capital_increase_by_cash' : capital_increase_by_cash,
                'capital_increase_by_earnings' : capital_increase_by_earnings,
                'capital_increase_by_surplus' : capital_increase_by_surplus, 
            },
            'category_field' : 'year',
        })
        path = self.__build_path(param)
        self.__save(json, path)

    def __build_path(self, param):
        if 'path' in param:
            return param['path']
        else:
            relative_path = '''{key}.json'''.format(key=param['stock_symbol'])
            return self.file_utils.join_paths(self.base_path, relative_path)

    def __save(self, json, path):
        self.json_utils.save(json, path)
        