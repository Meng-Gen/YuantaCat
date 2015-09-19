#-*- coding: utf-8 -*-

from yuantacat.spider.profitability_spider import ProfitabilitySpider

import unittest

class ProfitabilitySpiderTest(unittest.TestCase):
    def test_crawl_2498(self):
        spider = ProfitabilitySpider()
        param = { 'stock_symbol' : '2498' }
        spider.crawl(param)
        self.assertTrue(spider.is_crawled(param))
