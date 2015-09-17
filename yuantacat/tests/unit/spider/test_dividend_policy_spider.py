#-*- coding: utf-8 -*-

from yuantacat.spider.dividend_policy_spider import DividendPolicySpider

import unittest

class DividendPolicySpiderTest(unittest.TestCase):
    def setUp(self):
        self.spider = DividendPolicySpider()

    def tearDown(self):
        self.spider = None

    def test_crawl_2498(self):
        param = { 'stock_symbol' : '2498' }
        self.spider.crawl(param)
        self.assertTrue(self.spider.is_crawled(param))
