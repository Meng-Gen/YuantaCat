#-*- coding: utf-8 -*-

from yuantacat.dao.yuanta_dao import YuantaDao

class BalanceSheetSummaryDao(YuantaDao):
    def __init__(self, column_name_list, row_list, stock_symbol, period):
        YuantaDao.__init__(self, column_name_list, row_list, stock_symbol, period)

class BalanceSheetDao(YuantaDao):
    def __init__(self, column_name_list, row_list, stock_symbol, period):
        YuantaDao.__init__(self, column_name_list, row_list, stock_symbol, period)
