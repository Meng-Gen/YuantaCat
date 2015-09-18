#-*- coding: utf-8 -*-

from yuantacat.spider.balance_sheet_spider import BalanceSheetSummarySpider
from yuantacat.spider.balance_sheet_spider import BalanceSheetQuarterlySpider
from yuantacat.spider.balance_sheet_spider import BalanceSheetYearlySpider

import unittest

class BalanceSheetSpiderTest(unittest.TestCase):
    def test_crawl_summary_2498(self):
        spider = BalanceSheetSummarySpider()
        param = { 'stock_symbol' : '2498' }
        spider.crawl(param)
        self.assertTrue(spider.is_crawled(param))

    def test_crawl_quarterly_2498(self):
        spider = BalanceSheetQuarterlySpider()
        param = { 'stock_symbol' : '2498' }
        spider.crawl(param)
        self.assertTrue(spider.is_crawled(param))

    def test_crawl_yearly_2498(self):
        spider = BalanceSheetYearlySpider()
        param = { 'stock_symbol' : '2498' }
        spider.crawl(param)
        self.assertTrue(spider.is_crawled(param))
