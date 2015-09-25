#-*- coding: utf-8 -*-

from yuantacat.common.date_utils import DateUtils

class FinancialFeedBuilder():
    def build(self, dao):
        feed = []
        stock_symbol = dao.get_stock_symbol()
        release_date = DateUtils().now_date()
        stmt_date_list = dao.get_column_name_list()
        period = dao.get_period()
        row_list = dao.get_row_list()
        for i in range(len(row_list)):
            if not row_list[i]:
                continue
            account = row_list[i][0]
            for j in range(1, len(row_list[i])):
                entry = {
                    'release_date' : release_date,
                    'stock_symbol' : stock_symbol,
                    'stmt_date' : stmt_date_list[j], 
                    'account' : account,
                    'account_order' : i + 1,
                    'value' : row_list[i][j],
                    'period' : period,
                }
                feed.append(entry)
        return tuple(feed)
