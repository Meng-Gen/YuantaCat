#-*- coding: utf-8 -*-

from yuantacat.analyzer.operating_revenue_analyzer import OperatingRevenueAnalyzer
from yuantacat.report.data_creator import DataCreator

class OperatingRevenueDataCreator():
    def __init__(self):
        self.data_creator = DataCreator()

    def create(self, param):
        create_param = {
            'stock_symbol' : param['stock_symbol'], 
            'data' : self.__build_data_param(param),
            'category_field' : 'date',
            'base_path' : './report/chart/operating_revenue/',
        }
        return self.data_creator.create(create_param)

    def __build_data_param(self, param):
        analyzer = OperatingRevenueAnalyzer(stock_symbol=param['stock_symbol'])
        operating_revenue = analyzer.get_operating_revenue().get()
        accumulated_operating_revenue = analyzer.get_accumulated_operating_revenue().get()
        accumulated_operating_revenue_yoy = analyzer.get_accumulated_operating_revenue_yoy().get()
        long_term_average = analyzer.get_long_term_average().get()
        short_term_average = analyzer.get_short_term_average().get()
        return {
            'operating_revenue' : { 
                'value' : operating_revenue,
                'format' : 'integer',
            },
            'accumulated_operating_revenue' : {
                'value' : accumulated_operating_revenue,
                'format' : 'integer',
            },
            'accumulated_operating_revenue_yoy' : {
                'value' : accumulated_operating_revenue_yoy,
                'format' : 'percentage',
            },
            'long_term_average' : {
                'value' : long_term_average,
                'format' : 'integer',
            },
            'short_term_average' : {
                'value' : short_term_average,
                'format' : 'integer',
            },
        }
