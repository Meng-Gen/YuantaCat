#-*- coding: utf-8 -*-

from yuantacat.analyzer.kn_analyzer import KnAnalyzer
from yuantacat.report.data_creator import DataCreator

class KnDataCreator():
    def __init__(self):
        self.data_creator = DataCreator()

    def create(self, param):
        create_param = {
            'stock_symbol' : param['stock_symbol'], 
            'data' : self.__build_data_param(param),
            'category_field' : 'date',
            'base_path' : self.__build_base_path(param),
        }
        return self.data_creator.create(create_param)

    def __build_data_param(self, param):
        analyzer = KnAnalyzer(stock_symbol=param['stock_symbol'], period=param['period'])
        min_kn = analyzer.get_min_kn().get()
        max_kn = analyzer.get_max_kn().get()
        return {
            'min_kn' : { 
                'value' : min_kn,
                'format' : 'percentage',
            },
            'max_kn' : {
                'value' : max_kn,
                'format' : 'percentage',
            },
        }

    def __build_base_path(self, param):
        if param['period'] == 'Y':
            return './report/chart/data/kn/yearly/'
        elif param['period'] == 'Q':
            return './report/chart/data/kn/quarterly/'
