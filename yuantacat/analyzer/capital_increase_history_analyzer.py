#-*- coding: utf-8 -*-

from yuantacat.database.database import Database
from yuantacat.common.analyzer_utils import AnalyzerUtils

class CapitalIncreaseHistoryAnalyzer():
    def __init__(self):
        self.database = Database()
        self.analyzer_utils = AnalyzerUtils()

    def get_capital_increase_by_cash(self, stock_symbol):
        records = self.database.get('CapitalIncreaseByCash', { 'stock_symbol' : stock_symbol })
        return self.analyzer_utils.get_time_series(records)

    def get_capital_increase_by_earnings(self, stock_symbol):
        records = self.database.get('CapitalIncreaseByEarnings', { 'stock_symbol' : stock_symbol })
        return self.analyzer_utils.get_time_series(records)

    def get_capital_increase_by_surplus(self, stock_symbol):
        records = self.database.get('CapitalIncreaseBySurplus', { 'stock_symbol' : stock_symbol })
        return self.analyzer_utils.get_time_series(records)
