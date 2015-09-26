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
                'Assets',
                'Sales', 
            ]
        }
        self.time_series = AccountTimeSeries(param)
        self.period = period

    def get_roe(self):
        # ROE = NetIncome / Equity
        net_income = self.time_series.get('NetIncome')
        equity = self.time_series.get('Equity').get_average()
        return net_income / equity

    def get_roa(self):
        # ROE = NetIncome / Assets
        net_income = self.time_series.get('NetIncome')
        assets = self.time_series.get('Assets').get_average()
        return net_income / assets

    def get_ros(self):
        # ROS (returns on sales) = NetIncome / Sales
        net_income = self.time_series.get('NetIncome')
        sales = self.time_series.get('Sales') 
        return net_income / sales

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
