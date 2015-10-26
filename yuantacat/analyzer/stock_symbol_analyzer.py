#-*- coding: utf-8 -*-

from yuantacat.database.database import Database

class StockSymbolAnalyzer():
    def __init__(self):
        self.database = Database()
        self.market_category = {
            '\xe4\xb8\x8a\xe5\xb8\x82' : 'TW',
            '\xe4\xb8\x8a\xe6\xab\x83' : 'TWO',
        }

    def get_stock_symbol_list(self):
        result = []
        records = self.database.get('StockSymbolList', None)
        for record in records:
            entry = { 
                'stock_symbol' : record[0], 
                'listing_date' : record[1], 
                'market_category' : self.market_category[record[2]] 
            }
            result.append(entry)
        return result
