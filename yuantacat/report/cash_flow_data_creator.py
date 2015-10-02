#-*- coding: utf-8 -*-

from yuantacat.analyzer.cash_flow_analyzer import CashFlowAnalyzer
from yuantacat.report.data_creator import DataCreator

class CashFlowDataCreator():
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
        analyzer = CashFlowAnalyzer(stock_symbol=param['stock_symbol'], period=param['period'])
        net_profit = analyzer.get_net_profit().get()
        cash_flow_from_operating_activities = analyzer.get_cash_flow_from_operating_activities().get()
        cash_flow_from_investing_activities = analyzer.get_cash_flow_from_investing_activities().get()
        cash_flow_from_financing_activities = analyzer.get_cash_flow_from_financing_activities().get()
        free_cash_flow = analyzer.get_free_cash_flow().get()
        accumulated_free_cash_flow = analyzer.get_accumulated_free_cash_flow().get()
        long_term_investments_to_assets_ratio = analyzer.get_long_term_investments_to_assets_ratio().get()
        return {
            'net_profit' : { 
                'value' : net_profit,
                'format' : 'integer',
            },
            'cash_flow_from_operating_activities' : {
                'value' : cash_flow_from_operating_activities,
                'format' : 'integer',
            },
            'cash_flow_from_investing_activities' : {
                'value' : cash_flow_from_investing_activities,
                'format' : 'integer',
            },
            'cash_flow_from_financing_activities' : {
                'value' : cash_flow_from_financing_activities,
                'format' : 'integer',
            },
            'free_cash_flow' : {
                'value' : free_cash_flow,
                'format' : 'integer',
            },
            'accumulated_free_cash_flow' : {
                'value' : accumulated_free_cash_flow,
                'format' : 'integer',
            },
            'long_term_investments_to_assets_ratio' : {
                'value' : long_term_investments_to_assets_ratio,
                'format' : 'percentage',
            },
        }

    def __build_base_path(self, param):
        if param['period'] == 'Y':
            return './report/chart/data/cash_flow/yearly/'
        elif param['period'] == 'Q':
            return './report/chart/data/cash_flow/quarterly/'
