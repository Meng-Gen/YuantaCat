#-*- coding: utf-8 -*-

from yuantacat.analyzer.account_time_series import AccountTimeSeries
from yuantacat.common.time_series import TimeSeries

class CashFlowAnalyzer():
    def __init__(self, stock_symbol, period):
        param = {
            'stock_symbol' : stock_symbol,
            'period' : period, 
            'account_list' : [
                'NetProfit',
                'CashFlowFromOperatingActivities',
                'CashFlowFromInvestingActivities',
                'CashFlowFromFinancingActivities',
                'LongTermInvestments',
                'Assets',
            ]
        }
        self.time_series = AccountTimeSeries(param)
        self.period = period

    def get_net_profit(self):
        net_profit = self.time_series.get('NetProfit')
        return net_profit

    def get_cash_flow_from_operating_activities(self):
        cash_flow = self.time_series.get('CashFlowFromOperatingActivities')
        return cash_flow

    def get_cash_flow_from_investing_activities(self):
        cash_flow = self.time_series.get('CashFlowFromInvestingActivities')
        return cash_flow

    def get_cash_flow_from_financing_activities(self):
        cash_flow = self.time_series.get('CashFlowFromFinancingActivities')
        return cash_flow

    def get_free_cash_flow(self):
        # FreeCashFlow = CashFlowFromOperatingActivities + CashFlowFromInvestingActivities
        cash_flow_from_operating_activities = self.time_series.get('CashFlowFromOperatingActivities')
        cash_flow_from_investing_activities = self.time_series.get('CashFlowFromInvestingActivities')
        return cash_flow_from_operating_activities + cash_flow_from_investing_activities

    def get_accumulated_free_cash_flow(self):
        free_cash_flow = self.get_free_cash_flow()
        return free_cash_flow.accumulate()

    def get_long_term_investments_to_assets_ratio(self):
        long_term_investments = self.time_series.get('LongTermInvestments')
        assets = self.time_series.get('Assets')
        return long_term_investments / assets
