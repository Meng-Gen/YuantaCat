#-*- coding: utf-8 -*-

from yuantacat.database.database import Database

class StockSymbolAnalyzer():
    def __init__(self):
        self.database = Database()

    def get_stock_symbol_list(self):
        return self.database.get_stock_symbol_list()
