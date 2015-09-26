#-*- coding: utf-8 -*-

from yuantacat.analyzer.account_time_series import AccountTimeSeries
from yuantacat.common.time_series import TimeSeries

class DupontAnalyzer():
    def __init__(self, stock_symbol, period):
        param = {
            'stock_symbol' : stock_symbol,
            'period' : period, 
            'account_list' : [
                'NetIncome',
                'Equity',
            ]
        }
        self.time_series = AccountTimeSeries(param)
        self.period = period

    def get_roe(self):
        net_income = self.time_series.get('NetIncome')
        equity = self.time_series.get('Equity').get_average()
        return net_income / equity
