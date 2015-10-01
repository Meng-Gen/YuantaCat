#-*- coding: utf-8 -*-

from yuantacat.analyzer.capital_increase_history_analyzer import CapitalIncreaseHistoryAnalyzer
from yuantacat.report.data_creator import DataCreator

class CapitalIncreaseHistoryDataCreator():
    def __init__(self):
        self.data_creator = DataCreator()

    def create(self, param):
        create_param = {
            'stock_symbol' : param['stock_symbol'], 
            'data' : self.__build_data_param(param),
            'category_field' : 'year',
            'base_path' : './report/chart/capital_increase_history/',
        }
        return self.data_creator.create(create_param)

    def __build_data_param(self, param):
        stock_symbol = param['stock_symbol']
        analyzer = CapitalIncreaseHistoryAnalyzer(stock_symbol)
        capital_increase_by_cash = analyzer.get_capital_increase_by_cash().get()
        capital_increase_by_earnings = analyzer.get_capital_increase_by_earnings().get()
        capital_increase_by_surplus = analyzer.get_capital_increase_by_surplus().get()
        return {
            'capital_increase_by_cash' : { 
                'value' : capital_increase_by_cash,
                'format' : 'float',
            },
            'capital_increase_by_earnings' : {
                'value' : capital_increase_by_earnings,
                'format' : 'float', 
            },
            'capital_increase_by_surplus' : {
                'value' : capital_increase_by_surplus,
                'format' : 'float',
            }
        }
