#-*- coding: utf-8 -*-

from yuantacat.spider.income_statement_spider import IncomeStatementQuarterlySpider
from yuantacat.spider.income_statement_spider import IncomeStatementYearlySpider

import unittest

class IncomeStatementSpiderTest(unittest.TestCase):
    def test_crawl_quarterly_2498(self):
        spider = IncomeStatementQuarterlySpider()
        param = { 'stock_symbol' : '2498' }
        spider.crawl(param)
        self.assertTrue(spider.is_crawled(param))

    def test_crawl_yearly_2498(self):
        spider = IncomeStatementYearlySpider()
        param = { 'stock_symbol' : '2498' }
        spider.crawl(param)
        self.assertTrue(spider.is_crawled(param))
