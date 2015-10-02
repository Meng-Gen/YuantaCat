#-*- coding: utf-8 -*-

from yuantacat.analyzer.account_time_series import AccountTimeSeries
from yuantacat.common.time_series import TimeSeries

class CapitalStructureAnalyzer():
    def __init__(self, stock_symbol, period):
        param = {
            'stock_symbol' : stock_symbol,
            'period' : period, 
            'account_list' : [
                'Assets',
                'Liabilities',  
                'Equity',
                'LongTermLiabilities',
                'CurrentLiabilities',
                'FixedAssets',
            ]
        }
        self.time_series = AccountTimeSeries(param)
        self.period = period

    def get_equity_ratio(self):
        # EquityRatio = Equity / Assets
        equity = self.time_series.get('Equity')
        assets = self.time_series.get('Assets')
        return equity / assets

    def get_liabilities_ratio(self):
        # LiabilitiesRatio = Liabilities / Assets
        liabilities = self.time_series.get('Liabilities')
        assets = self.time_series.get('Assets')
        return liabilities / assets

    def get_equity_multiplier(self):
        # EquityMultiplier = Assets / Equity
        assets = self.time_series.get('Assets')
        equity = self.time_series.get('Equity')
        return assets / equity

    def get_true_liabilities_ratio(self):
        # TrueLiabilitiesRatio = LongTermLiabilities / (Assets - CurrentLiabilities)
        long_term_liabilities = self.time_series.get('LongTermLiabilities')
        assets = self.time_series.get('Assets')
        current_liabilities = self.time_series.get('CurrentLiabilities')
        return long_term_liabilities / (assets - current_liabilities)

    def get_long_term_capital_to_fixed_assets_ratio(self):
        # LongTermCapitalToFixedAssetsRatio = (LongTermLiabilities + Equity) / FixedAssets
        long_term_liabilities = self.time_series.get('LongTermLiabilities')
        equity = self.time_series.get('Equity')
        fixed_assets = self.time_series.get('FixedAssets')
        return (long_term_liabilities + equity) / fixed_assets
