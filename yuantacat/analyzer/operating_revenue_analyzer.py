#-*- coding: utf-8 -*-

from yuantacat.analyzer.account_time_series import AccountTimeSeries
from yuantacat.common.time_series import TimeSeries

class OperatingRevenueAnalyzer():
    def __init__(self, stock_symbol):
        param = {
            'stock_symbol' : stock_symbol,
            'account_list' : [
                'OperatingRevenue',
            ]
        }
        self.time_series = AccountTimeSeries(param)

    def get_operating_revenue(self):
        operating_revenue = self.time_series.get('OperatingRevenue')
        return operating_revenue

    def get_accumulated_operating_revenue(self):
        operating_revenue = self.time_series.get('OperatingRevenue')
        return operating_revenue.accumulate()

    def get_accumulated_operating_revenue_yoy(self):
        operating_revenue = self.time_series.get('OperatingRevenue')
        return operating_revenue.accumulate().get_yoy()

    def get_long_term_average(self):
        operating_revenue = self.time_series.get('OperatingRevenue')
        return operating_revenue.get_moving_average(12)

    def get_short_term_average(self):
        operating_revenue = self.time_series.get('OperatingRevenue')
        return operating_revenue.get_moving_average(3)
