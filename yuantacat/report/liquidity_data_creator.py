#-*- coding: utf-8 -*-

from yuantacat.analyzer.liquidity_analyzer import LiquidityAnalyzer
from yuantacat.report.data_creator import DataCreator

class LiquidityDataCreator():
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
        analyzer = LiquidityAnalyzer(stock_symbol=param['stock_symbol'], period=param['period'])
        current_ratio = analyzer.get_current_ratio().get()
        quick_ratio = analyzer.get_quick_ratio().get()
        interest_protection_multiples = analyzer.get_interest_protection_multiples().get()
        return {
            'current_ratio' : { 
                'value' : current_ratio,
                'format' : 'float',
            },
            'quick_ratio' : {
                'value' : quick_ratio,
                'format' : 'float',
            },
            'interest_protection_multiples' : {
                'value' : interest_protection_multiples,
                'format' : 'float',
            },
        }

    def __build_base_path(self, param):
        if param['period'] == 'Y':
            return './yuantacat/data/report/liquidity/yearly/'
        elif param['period'] == 'Q':
            return './yuantacat/data/report/liquidity/quarterly/'
