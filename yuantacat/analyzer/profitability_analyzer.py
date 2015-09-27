#-*- coding: utf-8 -*-

from yuantacat.analyzer.account_time_series import AccountTimeSeries
from yuantacat.common.time_series import TimeSeries

class ProfitabilityAnalyzer():
    def __init__(self, stock_symbol, period):
        param = {
            'stock_symbol' : stock_symbol,
            'period' : period, 
            'account_list' : [
                'Sales',
                'GrossProfit',
                'OperatingProfit',
                'NetProfit',
                'IncomeBeforeTax'
            ]
        }
        self.time_series = AccountTimeSeries(param)
        self.period = period

    def get_gross_profit_margin(self):
        # GrossProfitMargin = GrossProfit / Sales
        gross_profit = self.time_series.get('GrossProfit')
        sales = self.time_series.get('Sales')
        return gross_profit / sales

    def get_operating_profit_margin(self):
        # OperatingProfitMargin = OperatingProfit / Sales
        operating_profit = self.time_series.get('OperatingProfit')
        sales = self.time_series.get('Sales')
        return operating_profit / sales
    
    def get_net_profit_before_tax_margin(self):
        # NetProfitBeforeTaxMargin = NetProfit / Sales
        net_profit_before_tax = self.time_series.get('IncomeBeforeTax')
        sales = self.time_series.get('Sales')
        return net_profit_before_tax / sales

    def get_net_profit_margin(self):
        # NetProfitMargin = NetProfit / Sales
        net_profit = self.time_series.get('NetProfit')
        sales = self.time_series.get('Sales')
        return net_profit / sales