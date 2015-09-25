#-*- coding: utf-8 -*-

from yuantacat.database.database import Database
from yuantacat.common.time_series import TimeSeries

class AccountTimeSeries():
    def __init__(self, param):
        self.value = self.__init_value(param)

    def __init_value(self, param):
        output = {}
        database = Database()
        for account in param['account_list']:
            output[account] = TimeSeries.create(database.get(account, param))
        return output

    def get(self, account):
        return self.value[account]
