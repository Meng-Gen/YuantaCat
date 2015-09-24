#-*- coding: utf-8 -*-

from yuantacat.analyzer.analyzer_time_series import AnalyzerTimeSeries

class CapitalIncreaseHistoryAnalyzer():
    def __init__(self, stock_symbol):
        self.time_series = AnalyzerTimeSeries(stock_symbol, [
            'CapitalIncreaseByCash', 
            'CapitalIncreaseByEarnings',
            'CapitalIncreaseBySurplus',
        ])

    def get_capital_increase_by_cash(self):
        return self.time_series.get('CapitalIncreaseByCash')

    def get_capital_increase_by_earnings(self):
        return self.time_series.get('CapitalIncreaseByEarnings')

    def get_capital_increase_by_surplus(self):
        return self.time_series.get('CapitalIncreaseBySurplus')
