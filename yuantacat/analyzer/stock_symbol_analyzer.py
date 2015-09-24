#-*- coding: utf-8 -*-

from yuantacat.database.database import Database

class StockSymbolAnalyzer():
    def __init__(self):
        self.database = Database()

    def get_stock_symbol_list(self):
        records = self.database.get('StockSymbolList', None)
        return [{ 'stock_symbol' : record[0], 'listing_date' : record[1] } for record in records]
