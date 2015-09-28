#-*- coding: utf-8 -*-

from yuantacat.analyzer.account_time_series import AccountTimeSeries
from yuantacat.common.time_series import TimeSeries

class LiquidityAnalyzer():
    def __init__(self, stock_symbol, period):
        param = {
            'stock_symbol' : stock_symbol,
            'period' : period, 
            'account_list' : [
                'CurrentAssets',
                'CurrentLiabilities',  
                'Inventories',
                'PrepaidAccounts',
                'IncomeBeforeTax',
                'InterestExpense',
            ]
        }
        self.time_series = AccountTimeSeries(param)
        self.period = period

    def get_current_ratio(self):
        # CurrentRatio = CurrentAssets / CurrentLiabilities
        current_assets = self.time_series.get('CurrentAssets')
        current_liabilities = self.time_series.get('CurrentLiabilities')
        return current_assets / current_liabilities

    def get_quick_ratio(self):
        # QuickAssets = CurrentAssets - Inventories - PrepaidAccounts
        current_assets = self.time_series.get('CurrentAssets')
        inventories = self.time_series.get('Inventories')
        prepaid_accounts = self.time_series.get('PrepaidAccounts')
        quick_assets = current_assets - inventories - prepaid_accounts

        # QuickRatio = QuickAssets / CurrentLiabilities
        current_liabilities = self.time_series.get('CurrentLiabilities')
        return quick_assets / current_liabilities

    def get_interest_protection_multiples(self):
        # InterestProtectionMultiples = EBDIT / InterestExpense
        # EBDIT = IncomeBeforeTax + InterestExpense
        income_before_tax = self.time_series.get('IncomeBeforeTax')
        interest_expense = self.time_series.get('InterestExpense')
        return (income_before_tax + interest_expense) / interest_expense
