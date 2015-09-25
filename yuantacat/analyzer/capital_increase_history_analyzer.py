#-*- coding: utf-8 -*-

from yuantacat.analyzer.account_time_series import AccountTimeSeries

class CapitalIncreaseHistoryAnalyzer():
    def __init__(self, stock_symbol):
        param = {
            'stock_symbol' : stock_symbol,
            'account_list' : [
                'CapitalIncreaseByCash', 
                'CapitalIncreaseByEarnings',
                'CapitalIncreaseBySurplus',
            ]
        }
        self.time_series = AccountTimeSeries(param)

    def get_capital_increase_by_cash(self):
        return self.time_series.get('CapitalIncreaseByCash')

    def get_capital_increase_by_earnings(self):
        return self.time_series.get('CapitalIncreaseByEarnings')

    def get_capital_increase_by_surplus(self):
        return self.time_series.get('CapitalIncreaseBySurplus')
