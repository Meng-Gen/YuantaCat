#-*- coding: utf-8 -*-

from yuantacat.spider.capital_increase_history_spider import CapitalIncreaseHistorySpider

import unittest

class CapitalIncreaseHistorySpiderTest(unittest.TestCase):
    def test_crawl_2498(self):
        spider = CapitalIncreaseHistorySpider()
        param = { 'stock_symbol' : '2498' }
        spider.crawl(param)
        self.assertTrue(spider.is_crawled(param))
