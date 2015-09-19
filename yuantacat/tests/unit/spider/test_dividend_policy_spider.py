#-*- coding: utf-8 -*-

from yuantacat.spider.dividend_policy_spider import DividendPolicySpider

import unittest

class DividendPolicySpiderTest(unittest.TestCase):
    def test_crawl_2498(self):
        spider = DividendPolicySpider()
        param = { 'stock_symbol' : '2498' }
        spider.crawl(param)
        self.assertTrue(spider.is_crawled(param))
