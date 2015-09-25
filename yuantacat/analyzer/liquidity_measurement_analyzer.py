#-*- coding: utf-8 -*-

from yuantacat.analyzer.account_time_series import AccountTimeSeries
from yuantacat.common.time_series import TimeSeries

class LiquidityMeasurementAnalyzer():
    def __init__(self, stock_symbol, period):
        param = {
            'stock_symbol' : stock_symbol,
            'period' : period, 
            'account_list' : [
                'CurrentAssets',
                'CurrentLiabilities',  
                'CashAndEquivalents',
                'MarketableSecurities',
                'AccountsReceivable',
            ]
        }
        self.time_series = AccountTimeSeries(param)
        self.period = period

    def get_current_ratio(self):
        # CurrentRatio = CurrentAssets / CurrentLiabilities
        current_assets = self.time_series.get('CurrentAssets')
        current_liabilities = self.time_series.get('CurrentLiabilities')
        return current_assets.divide(current_liabilities)

    def get_quick_ratio(self):
        # QuickRatio = QuickAssets / CurrentLiabilities
        # QuickAssets = CashAndEquivalents + MarketableSecurities + AccountsReceivable
        cash_and_equivalents = self.time_series.get('CashAndEquivalents')
        marketable_securities = self.time_series.get('MarketableSecurities')
        accounts_receivable = self.time_series.get('AccountsReceivable')
        quick_assets = cash_and_equivalents.add(marketable_securities).add(accounts_receivable)
        current_liabilities = self.time_series.get('CurrentLiabilities')
        return quick_assets.divide(current_liabilities)

    def get_cash_conversion_cycle(self):
        # CCC = DIO + DSO - DPO
        assets = self.time_series.get('Assets')
        equity = self.time_series.get('Equity')
        return assets.divide(equity)
