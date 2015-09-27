#-*- coding: utf-8 -*-

from yuantacat.analyzer.account_time_series import AccountTimeSeries
from yuantacat.common.time_series import TimeSeries

class DupontAnalyzer():
    def __init__(self, stock_symbol, period):
        param = {
            'stock_symbol' : stock_symbol,
            'period' : period, 
            'account_list' : [
                'NetProfit',
                'Equity',
                'Assets',
                'Sales', 
            ]
        }
        self.time_series = AccountTimeSeries(param)
        self.period = period

    def get_roe(self):
        # ROE = NetProfit / Equity
        net_profit = self.time_series.get('NetProfit')
        equity = self.time_series.get('Equity').get_average()
        return net_profit / equity

    def get_roa(self):
        # ROE = NetProfit / Assets
        net_profit = self.time_series.get('NetProfit')
        assets = self.time_series.get('Assets').get_average()
        return net_profit / assets

    def get_ros(self):
        # ROS (returns on sales) = NetProfit / Sales
        net_profit = self.time_series.get('NetProfit')
        sales = self.time_series.get('Sales') 
        return net_profit / sales

    def get_ato(self):
        # ATO (asset turnover) = Sales / Assets
        sales = self.time_series.get('Sales') 
        assets = self.time_series.get('Assets').get_average()
        return sales / assets        

    def get_equity_multiplier(self):
        # EquityMultiplier = Assets / Equity
        assets = self.time_series.get('Assets').get_average()
        equity = self.time_series.get('Equity').get_average()
        return assets / equity
