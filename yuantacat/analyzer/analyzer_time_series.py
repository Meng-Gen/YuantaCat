#-*- coding: utf-8 -*-

from yuantacat.database.database import Database
from yuantacat.common.time_series import TimeSeries

class AnalyzerTimeSeries():
    def __init__(self, stock_symbol, account_list):
        self.value = self.__init_value(stock_symbol, account_list)

    def __init_value(self, stock_symbol, account_list):
        output = {}
        database = Database()
        entry = { 'stock_symbol' : stock_symbol }
        for account in account_list:
            output[account] = TimeSeries.create(database.get(account, entry))
        return output

    def get(self, account):
        return self.value[account]
