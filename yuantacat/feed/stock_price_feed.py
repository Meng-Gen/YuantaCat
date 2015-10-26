#-*- coding: utf-8 -*-

from yuantacat.common.date_utils import DateUtils
from yuantacat.feed.feed import Feed

class StockPriceFeed(Feed):
    pass 

class StockPriceFeedBuilder():
    def build(self, dao):
        tuple_feed = self.__build_tuple(dao)
        return StockPriceFeed(tuple_feed)

    def __build_tuple(self, dao):    
        feed = []
        stock_symbol = dao.get_stock_symbol()
        release_date = DateUtils().now_date()
        column_name_list = dao.get_column_name_list()
        period = dao.get_period()
        row_list = dao.get_row_list()
        for row in row_list:
            stmt_date = row[0]
            for j in range(1, len(row)):
                entry = {
                    'release_date' : release_date,
                    'stock_symbol' : stock_symbol,
                    'stmt_date' : stmt_date, 
                    'account' : account,
                    'account_order' : j,
                    'value' : row[j],
                    'period' : period,
                }
                feed.append(entry)
        return tuple(feed)
