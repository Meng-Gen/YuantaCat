#-*- coding: utf-8 -*-

from yuantacat.analyzer.account_time_series import AccountTimeSeries
from yuantacat.common.time_series import TimeSeries

class FinancialStructureAnalyzer():
    def __init__(self, stock_symbol, period):
        param = {
            'stock_symbol' : stock_symbol,
            'period' : period, 
            'account_list' : [
                'Assets',
                'Liabilities',  
                'Equity',
            ]
        }
        self.time_series = AccountTimeSeries(param)
        self.period = period

    def get_liabilities_ratio(self):
        # LiabilitiesRatio = Liabilities / Assets
        liabilities = self.time_series.get('Liabilities')
        assets = self.time_series.get('Assets')
        return liabilities.divide(assets)

    def get_equity_ratio(self):
        # EquityRatio = Equity / Assets
        equity = self.time_series.get('Equity')
        assets = self.time_series.get('Assets')
        return equity.divide(assets)

    def get_equity_multiplier(self):
        # EquityMultiplier = Assets / Equity
        assets = self.time_series.get('Assets')
        equity = self.time_series.get('Equity')
        return assets.divide(equity)
