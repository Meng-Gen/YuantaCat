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
                'Inventories',
                'PrepaidAccounts',
                'CostOfGoodsSold',
                'Sales',
                'AccountsReceivable',
                'AccountsPayable', 
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

    def get_dio(self):
        # Inventory Turnover Ratio = Cost of goods sold / Inventory
        # DIO = 365 / Inventory Turnover Ratio 
        cost_of_goods_sold = self.time_series.get('CostOfGoodsSold')
        inventories = self.time_series.get('Inventories')
        inventory_turnover_ratio = cost_of_goods_sold / inventories.get_average()
        dio = inventory_turnover_ratio.get_inverse().scalar(365.0)
        return self.__annualize(dio)

    def get_dso(self):
        # Receivables Turnover Ratio = Sales / Accounts receivable
        # DSO = 365 / Receivables Turnover Ratio
        sales = self.time_series.get('Sales')
        accounts_receivable = self.time_series.get('AccountsReceivable')
        receivables_turnover_ratio = sales / accounts_receivable.get_average()
        dso = receivables_turnover_ratio.get_inverse().scalar(365.0)
        return self.__annualize(dso)

    def get_dpo(self):
        # AccountsPayableTurnoverRatio = Cost of goods sold / Accounts payable
        # DPO = 365 / AccountsPayableTurnoverRatio
        cost_of_goods_sold = self.time_series.get('CostOfGoodsSold')
        accounts_payable = self.time_series.get('AccountsPayable')
        accounts_payable_turnover_ratio = cost_of_goods_sold / accounts_payable.get_average()
        dpo = accounts_payable_turnover_ratio.get_inverse().scalar(365.0)
        return self.__annualize(dpo)

    def get_cash_conversion_cycle(self):
        # CCC = DIO + DSO - DPO
        dio = self.get_dio()
        dso = self.get_dso()
        dpo = self.get_dpo()
        return dio + dso - dpo

    def __annualize(self, time_series):
        if self.period == 'Y':
            return time_series
        elif self.period == 'Q':
            return time_series.scalar(0.25)
