#-*- coding: utf-8 -*-

from yuantacat.analyzer.analyzer_time_series import AnalyzerTimeSeries
from yuantacat.common.time_series import TimeSeries

class DupontAnalyzer():
    def __init__(self, stock_symbol):
        self.time_series = AnalyzerTimeSeries(stock_symbol, [
            'NetIncome',
            'Equity',
        ])

    def get_roe(self):
        net_income = self.time_series.get('NetIncome')
        equity = self.time_series.get('Equity').get_average()
        return net_income.divide(equity)
