#-*- coding: utf-8 -*-

from yuantacat.spider.stock_price_spider import StockPriceSpider

import unittest

class StockPriceSpiderTest(unittest.TestCase):
    def test_crawl_2498(self):
        spider = StockPriceSpider()
        param = { 
            'stock_symbol' : '2498',
            'market_type' : 'stock_exchange_market',
        }
        spider.crawl(param)
        self.assertTrue(spider.is_crawled(param))
