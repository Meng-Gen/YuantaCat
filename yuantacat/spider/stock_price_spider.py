#-*- coding: utf-8 -*-

from yuantacat.spider.spider import Spider

class StockPriceSpider(Spider):
    def build_url(self, param):
        return '''http://real-chart.finance.yahoo.com/table.csv?s=%s.%s&ignore=.csv''' \
                % (param['stock_symbol'], param['market_category'])

    def build_key(self, param):
        return '''stock_price/%s''' % (param['stock_symbol'])
