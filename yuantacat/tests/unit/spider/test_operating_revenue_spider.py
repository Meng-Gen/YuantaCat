#-*- coding: utf-8 -*-

from yuantacat.spider.operating_revenue_spider import OperatingRevenueSpider

import unittest

class OperatingRevenueSpiderTest(unittest.TestCase):
    def setUp(self):
        self.spider = OperatingRevenueSpider()

    def tearDown(self):
        self.spider = None

    def test_crawl_2498(self):
        param = { 'stock_symbol' : '2498' }
        self.spider.crawl(param)
        self.assertTrue(self.spider.is_crawled(param))
