#-*- coding: utf-8 -*-

from yuantacat.spider.cash_flow_spider import CashFlowQuarterlySpider
from yuantacat.spider.cash_flow_spider import CashFlowYearlySpider

import unittest

class CashFlowSpiderTest(unittest.TestCase):
    def test_crawl_quarterly_2498(self):
        spider = CashFlowQuarterlySpider()
        param = { 'stock_symbol' : '2498' }
        spider.crawl(param)
        self.assertTrue(spider.is_crawled(param))

    def test_crawl_yearly_2498(self):
        spider = CashFlowYearlySpider()
        param = { 'stock_symbol' : '2498' }
        spider.crawl(param)
        self.assertTrue(spider.is_crawled(param))
