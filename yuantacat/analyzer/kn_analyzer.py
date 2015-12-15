#-*- coding: utf-8 -*-

from yuantacat.analyzer.account_time_series import AccountTimeSeries
from yuantacat.common.time_series import TimeSeries

class KnAnalyzer():
    def __init__(self, stock_symbol, period):
        param = {
            'stock_symbol' : stock_symbol,
            'period' : period, 
            'account_list' : [
                'NetProfit',
                'Equity',
                'StockPrice',
                'BookValue',
            ]
        }
        self.time_series = AccountTimeSeries(param)
        self.period = period

    def get_roe(self):
        # ROE = NetProfit / Equity
        net_profit = self.time_series.get('NetProfit')
        assets = self.time_series.get('Equity').get_average()
        return net_profit / assets

    def get_max_pbr(self):
        # max(PBR) = max(StockPrice) / BookValue
        stock_price = self.time_series.get('StockPrice')
        book_value = self.time_series.get('BookValue')
        return stock_price.get_max_by_period(self.period) / book_value

    def get_min_pbr(self):
        # min(PBR) = min(StockPrice) / BookValue
        stock_price = self.time_series.get('StockPrice')
        book_value = self.time_series.get('BookValue')
        return stock_price.get_min_by_period(self.period) / book_value

    def get_max_kn(self):
        # max(Kn) = ROE / min(PBR)
        roe = self.get_roe().annualize(self.period)
        min_pbr = self.get_min_pbr()
        return roe / min_pbr

    def get_min_kn(self):
        # min(Kn) = ROE / max(PBR)        
        roe = self.get_roe().annualize(self.period)
        max_pbr = self.get_max_pbr()
        return roe / max_pbr
