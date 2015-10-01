#-*- coding: utf-8 -*-

from yuantacat.analyzer.revenue_index_analyzer import RevenueIndexAnalyzer
from yuantacat.report.data_creator import DataCreator

class RevenueIndexDataCreator():
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
        analyzer = RevenueIndexAnalyzer(stock_symbol=param['stock_symbol'], period=param['period'])
        inventory_index = analyzer.get_inventory_index().get()
        accounts_receivable_index = analyzer.get_accounts_receivable_index().get()
        gross_profit_index = analyzer.get_gross_profit_index().get()
        selling_and_administrative_expenses_index = analyzer.get_selling_and_administrative_expenses_index().get()
        accounts_payable_index = analyzer.get_accounts_payable_index().get()
        return {
            'inventory_index' : { 
                'value' : inventory_index,
                'format' : 'float',
            },
            'accounts_receivable_index' : {
                'value' : accounts_receivable_index,
                'format' : 'float',
            },
            'gross_profit_index' : {
                'value' : gross_profit_index,
                'format' : 'float',
            },
            'selling_and_administrative_expenses_index' : {
                'value' : selling_and_administrative_expenses_index,
                'format' : 'float',
            },
            'accounts_payable_index' : {
                'value' : accounts_payable_index,
                'format' : 'float',
            },
        }

    def __build_base_path(self, param):
        if param['period'] == 'Y':
            return './report/chart/revenue_index/yearly/'
        elif param['period'] == 'Q':
            return './report/chart/revenue_index/quarterly/'
