#-*- coding: utf-8 -*-

from yuantacat.analyzer.account_time_series import AccountTimeSeries
from yuantacat.common.time_series import TimeSeries

class RevenueIndexAnalyzer():
    def __init__(self, stock_symbol, period):
        param = {
            'stock_symbol' : stock_symbol,
            'period' : period, 
            'account_list' : [
                'Inventories',
                'Sales', 
                'AccountsReceivable',
                'GrossProfit',
                'SellingExpenses',
                'AdministrativeExpenses',
                'AccountsPayable',
            ]
        }
        self.time_series = AccountTimeSeries(param)
        self.period = period

    def get_inventory_index(self):
        # InventoryIndex = InventoryGrowthRate - SalesGrowthRate
        inventory_growth_rate = self.__get_growth_rate('Inventories')
        sales_growth_rate = self.__get_growth_rate('Sales')
        return inventory_growth_rate - sales_growth_rate

    def get_accounts_receivable_index(self):
        # AccountsReceivableIndex = AccountsReceivableGrowthRate - SalesGrowthRate
        accounts_receivable_growth_rate = self.__get_growth_rate('AccountsReceivable')
        sales_growth_rate = self.__get_growth_rate('Sales')
        return accounts_receivable_growth_rate - sales_growth_rate

    def get_gross_profit_index(self):
        # GrossProfitIndex = SalesGrowthRate - GrossProfitGrowthRate
        sales_growth_rate = self.__get_growth_rate('Sales')
        gross_profit_growth_rate = self.__get_growth_rate('GrossProfit')
        return sales_growth_rate - gross_profit_growth_rate

    def get_selling_and_administrative_expenses_index(self):
        # SellingAndAdministrativeExpensesIndex = SellingAndAdministrativeExpensesGrowthRate - SalesGrowthRate
        selling_expenses = self.time_series.get('SellingExpenses')
        administrative_expenses = self.time_series.get('AdministrativeExpenses')
        selling_and_administrative_expenses = selling_expenses + administrative_expenses
        selling_and_administrative_expenses_growth_rate \
                = self.__get_growth_rate_by_curr_time_series(selling_and_administrative_expenses)
        sales_growth_rate = self.__get_growth_rate('Sales')
        return selling_and_administrative_expenses_growth_rate - sales_growth_rate

    def get_accounts_payable_index(self):
        # AccountsPayableIndex = SalesGrowthRate - AccountsPayableGrowthRate
        sales_growth_rate = self.__get_growth_rate('Sales')
        accounts_payable_growth_rate = self.__get_growth_rate('AccountsPayable')
        return sales_growth_rate - accounts_payable_growth_rate

    def __get_growth_rate(self, account):
        curr_time_series = self.time_series.get(account)
        return self.__get_growth_rate_by_curr_time_series(curr_time_series)

    def __get_growth_rate_by_curr_time_series(self, curr_time_series):
        prev_time_series = curr_time_series.get_average().shift()
        return (curr_time_series - prev_time_series) / prev_time_series
