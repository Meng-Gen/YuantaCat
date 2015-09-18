#-*- coding: utf-8 -*-

from yuantacat.common.date_utils import DateUtils

class YuantaFeedBuilder():
    def __init__(self, column_name_list, value_index_list):
        self.date_utils = DateUtils()
        self.column_name_list = column_name_list
        self.value_index_list = value_index_list

    def build(self, dao):
        feed = []
        stock_symbol = dao.get_stock_symbol()
        release_date = self.date_utils.now_date()
        entry_count = len(self.column_name_list)
        for row in dao.get_row_list():
            stmt_date = row[0]
            value_list = [row[i] for i in self.value_index_list]
            for i in range(entry_count):
                entry = {
                    'release_date' : release_date,
                    'stock_symbol' : stock_symbol,
                    'stmt_date' : stmt_date, 
                    'account' : self.column_name_list[i],
                    'account_order' : i + 1,
                    'value' : value_list[i],
                }
                feed.append(entry)
        return tuple(feed)
