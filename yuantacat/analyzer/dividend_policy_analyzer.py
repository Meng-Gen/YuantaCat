#-*- coding: utf-8 -*-

from yuantacat.analyzer.account_time_series import AccountTimeSeries

class DividendPolicyAnalyzer():
    def __init__(self, stock_symbol):
        param = {
            'stock_symbol' : stock_symbol,
            'account_list' : [
                'CashDividends', 
                'StockDividendsFromRetainedEarnings',
                'StockDividendsFromCapitalReserve',
                'EmployeeStockBonusRatio',
            ]
        }
        self.time_series = AccountTimeSeries(param)

    def get_cash_dividends(self):
        return self.time_series.get('CashDividends')

    def get_stock_dividends_from_retained_earnings(self):
        return self.time_series.get('StockDividendsFromRetainedEarnings')

    def get_stock_dividends_from_capital_reserve(self):
        return self.time_series.get('StockDividendsFromCapitalReserve')

    def get_stock_dividends(self):
        # StockDividends = StockDividendsFromRetainedEarnings + StockDividendsFromCapitalReserve
        stock_dividends_from_retained_earnings = self.get_stock_dividends_from_retained_earnings()
        stock_dividends_from_capital_reserve = self.get_stock_dividends_from_capital_reserve()
        return stock_dividends_from_retained_earnings + stock_dividends_from_capital_reserve

    def get_employee_stock_bonus_ratio(self):
        return self.time_series.get('EmployeeStockBonusRatio')
