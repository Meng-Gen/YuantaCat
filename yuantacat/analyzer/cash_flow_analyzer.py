#-*- coding: utf-8 -*-

from yuantacat.analyzer.account_time_series import AccountTimeSeries
from yuantacat.common.time_series import TimeSeries

class CashFlowAnalyzer():
    def __init__(self, stock_symbol, period):
        param = {
            'stock_symbol' : stock_symbol,
            'period' : period, 
            'account_list' : [
                'NetIncome',
                'CashFlowFromOperatingActivities',
                'CashFlowFromInvestingActivities',
                'CashFlowFromFinancingActivities',
            ]
        }
        self.time_series = AccountTimeSeries(param)
        self.period = period

    def get_net_income(self):
        net_income = self.time_series.get('NetIncome')
        return net_income

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
