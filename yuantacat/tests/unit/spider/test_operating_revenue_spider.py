#-*- coding: utf-8 -*-

from yuantacat.spider.operating_revenue_spider import OperatingRevenueSpider

import unittest

class OperatingRevenueSpiderTest(unittest.TestCase):
    def test_crawl_2498(self):
        spider = OperatingRevenueSpider()
        param = { 'stock_symbol' : '2498' }
        spider.crawl(param)
        self.assertTrue(spider.is_crawled(param))
