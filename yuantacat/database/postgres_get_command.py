#-*- coding: utf-8 -*-

import psycopg2

class PostgresGetCommnad():
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.operation_map = {
            'StockSymbolList' : "select stock_symbol, listing_date from stock_symbol where release_date in (select max(release_date) from stock_symbol) and cfi_code = 'ESVUFR'",
            'CapitalIncreaseByCash' : u"select release_date, stmt_date, value from capital_increase_history where stock_symbol = %(stock_symbol)s and account = '現金增資'",
            'CapitalIncreaseByEarnings' : u"select release_date, stmt_date, value from capital_increase_history where stock_symbol = %(stock_symbol)s and account = '盈餘轉增資'",
            'CapitalIncreaseBySurplus' : u"select release_date, stmt_date, value from capital_increase_history where stock_symbol = %(stock_symbol)s and account = '公積及其他'",
        }

    def get(self, operation, param):
        connection = psycopg2.connect(self.connection_string)
        cursor = connection.cursor()
        cursor.execute(self.operation_map[operation], param)
        records = cursor.fetchall()
        connection.commit()
        connection.close()
        return records
