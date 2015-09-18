#-*- coding: utf-8 -*-

from yuantacat.spider.stock_symbol_spider import StockSymbolSpider

import unittest

class StockSymbolSpiderTest(unittest.TestCase):
    def test_crawl_stock_exchange_market(self):
        spider = StockSymbolSpider()
        param = { 'market_type' : 'stock_exchange_market' }
        spider.crawl(param)
        self.assertTrue(spider.is_crawled(param))

    def test_crawl_otc_market(self):
        spider = StockSymbolSpider()
        param = { 'market_type' : 'otc_market' }
        spider.crawl(param)
        self.assertTrue(spider.is_crawled(param))
