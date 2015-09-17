#-*- coding: utf-8 -*-

from yuantacat.common.date_utils import DateUtils

class TupleFeedBuilder():
    def __init__(self):
        self.date_utils = DateUtils()

    def build(self, dao):
        feed = []
        release_date = self.date_utils.now_date()
        stock_symbol = dao.get_stock_symbol()
        column_name_list = dao.get_column_name_list()
        stmt_date_list = column_name_list[1:] # the first column is account
        stmt_date_list = self.__flatten_stmt_date_list(stmt_date_list)
        stmt_date_len = len(stmt_date_list)

        account_order = 1
        for row in dao.get_row_list():
            account = row[0]
            number_list = row[1:]
            number_len = len(number_list)
            for i in range(stmt_date_len):
                stmt_date = stmt_date_list[i]
                value = number_list[i] if i < number_len else None
                entry = {
                    'release_date' : release_date,
                    'stock_symbol' : stock_symbol,
                    'stmt_date' : stmt_date, 
                    'account' : account,
                    'account_order' : account_order,
                    'value' : value
                }
                feed.append(entry)
            account_order += 1
        return tuple(feed)

    # flatten to date if stmt_date_list if date period list
    def __flatten_stmt_date_list(self, stmt_date_list):
        # if date period, we flatten to end date because begin date is always 
        # the first date of this year. 
        if len(stmt_date_list) > 0 and isinstance(stmt_date_list[0], tuple):
            return [stmt_date[1] for stmt_date in stmt_date_list]
        else:
            return stmt_date_list
