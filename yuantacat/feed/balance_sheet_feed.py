#-*- coding: utf-8 -*-

from yuantacat.feed.feed import Feed
from yuantacat.common.date_utils import DateUtils

class BalanceSheetFeed(Feed):
    pass 

class BalanceSheetFeedBuilder():
    def build(self, dao):
        tuple_feed = self.__build_tuple(dao)
        return BalanceSheetFeed(tuple_feed)

    def __build_tuple(self, dao):    
        feed = []
        stock_symbol = dao.get_stock_symbol()
        release_date = DateUtils().now_date()
        stmt_date_list = dao.get_column_name_list()
        entry_count = len(stmt_date_list)
        row_list = dao.get_row_list()
        for i in range(len(row_list)):
            account = row_list[i][0]
            for j in range(1, entry_count):
                entry = {
                    'release_date' : release_date,
                    'stock_symbol' : stock_symbol,
                    'stmt_date' : stmt_date_list[j], 
                    'account' : account,
                    'account_order' : i + 1,
                    'value' : row_list[i][j],
                }
                feed.append(entry)
        return tuple(feed)
