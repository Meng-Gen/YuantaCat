#-*- coding: utf-8 -*-

from yuantacat.analyzer.capital_structure_analyzer import CapitalStructureAnalyzer
from yuantacat.report.data_creator import DataCreator

class CapitalStructureDataCreator():
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
        analyzer = CapitalStructureAnalyzer(stock_symbol=param['stock_symbol'], period=param['period'])
        equity_ratio = analyzer.get_equity_ratio().get()
        liabilities_ratio = analyzer.get_liabilities_ratio().get()
        true_liabilities_ratio = analyzer.get_true_liabilities_ratio().get()
        equity_multiplier = analyzer.get_equity_multiplier().get()
        long_term_capital_to_fixed_assets_ratio = analyzer.get_long_term_capital_to_fixed_assets_ratio().get()
        return {
            'equity_ratio' : { 
                'value' : equity_ratio,
                'format' : 'percentage',
            },
            'liabilities_ratio' : {
                'value' : liabilities_ratio,
                'format' : 'percentage',
            },
            'true_liabilities_ratio' : {
                'value' : true_liabilities_ratio,
                'format' : 'percentage',
            },
            'equity_multiplier' : {
                'value' : equity_multiplier,
                'format' : 'float',
            },
            'long_term_capital_to_fixed_assets_ratio' : {
                'value' : long_term_capital_to_fixed_assets_ratio,
                'format' : 'float',
            },
        }

    def __build_base_path(self, param):
        if param['period'] == 'Y':
            return './report/chart/capital_structure/yearly/'
        elif param['period'] == 'Q':
            return './report/chart/capital_structure/quarterly/'
