#-*- coding: utf-8 -*-

from yuantacat.dao.yuanta_dao import YuantaDao

class BalanceSheetSummaryDao(YuantaDao):
    def __init__(self, column_name_list, row_list, stock_symbol):
        YuantaDao.__init__(self, column_name_list, row_list, stock_symbol)

class BalanceSheetQuarterlyDao(YuantaDao):
    def __init__(self, column_name_list, row_list, stock_symbol):
        YuantaDao.__init__(self, column_name_list, row_list, stock_symbol)

class BalanceSheetYearlyDao(YuantaDao):
    def __init__(self, column_name_list, row_list, stock_symbol):
        YuantaDao.__init__(self, column_name_list, row_list, stock_symbol)
