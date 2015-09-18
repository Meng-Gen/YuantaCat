#-*- coding: utf-8 -*-

from yuantacat.spider.profitability_spider import ProfitabilitySpider

import unittest

class ProfitabilitySpiderTest(unittest.TestCase):
    def setUp(self):
        self.spider = ProfitabilitySpider()

    def tearDown(self):
        self.spider = None

    def test_crawl_2498(self):
        param = { 'stock_symbol' : '2498' }
        self.spider.crawl(param)
        self.assertTrue(self.spider.is_crawled(param))
