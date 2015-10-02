#-*- coding: utf-8 -*-

from yuantacat.analyzer.dividend_policy_analyzer import DividendPolicyAnalyzer
from yuantacat.report.data_creator import DataCreator

class DividendPolicyDataCreator():
    def __init__(self):
        self.data_creator = DataCreator()

    def create(self, param):
        create_param = {
            'stock_symbol' : param['stock_symbol'], 
            'data' : self.__build_data_param(param),
            'category_field' : 'year',
            'base_path' : './report/chart/data/dividend_policy/',
        }
        return self.data_creator.create(create_param)

    def __build_data_param(self, param):
        stock_symbol = param['stock_symbol']
        analyzer = DividendPolicyAnalyzer(stock_symbol)
        cash_dividends = analyzer.get_cash_dividends().get()
        stock_dividends_from_retained_earnings = analyzer.get_stock_dividends_from_retained_earnings().get()
        stock_dividends_from_capital_reserve = analyzer.get_stock_dividends_from_capital_reserve().get()
        stock_dividends = analyzer.get_stock_dividends().get()
        employee_stock_bonus_ratio = analyzer.get_employee_stock_bonus_ratio().get()
        return {
            'cash_dividends' : { 
                'value' : cash_dividends,
                'format' : 'float',
            },
            'stock_dividends_from_retained_earnings' : {
                'value' : stock_dividends_from_retained_earnings,
                'format' : 'float', 
            },
            'stock_dividends_from_capital_reserve' : {
                'value' : stock_dividends_from_capital_reserve,
                'format' : 'float',
            },
            'stock_dividends' : {
                'value' : stock_dividends,
                'format' : 'float',
            },
            'employee_stock_bonus_ratio' : {
                'value' : employee_stock_bonus_ratio,
                'format' : 'percentage',
            },
        }
