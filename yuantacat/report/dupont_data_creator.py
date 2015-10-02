#-*- coding: utf-8 -*-

from yuantacat.analyzer.dupont_analyzer import DupontAnalyzer
from yuantacat.report.data_creator import DataCreator

class DupontDataCreator():
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
        analyzer = DupontAnalyzer(stock_symbol=param['stock_symbol'], period=param['period'])
        roe = analyzer.get_roe().get()
        roa = analyzer.get_roa().get()
        ros = analyzer.get_ros().get()
        ato = analyzer.get_ato().get()
        equity_multiplier = analyzer.get_equity_multiplier().get()
        return {
            'roe' : { 
                'value' : roe,
                'format' : 'percentage',
            },
            'roa' : {
                'value' : roa,
                'format' : 'percentage',
            },
            'ros' : {
                'value' : ros,
                'format' : 'percentage', 
            },
            'ato' : {
                'value' : ato,
                'format' : 'percentage',
            },
            'equity_multiplier' : {
                'value' : equity_multiplier,
                'format' : 'float',
            },
        }

    def __build_base_path(self, param):
        if param['period'] == 'Y':
            return './report/chart/data/dupont/yearly/'
        elif param['period'] == 'Q':
            return './report/chart/data/dupont/quarterly/'
