#-*- coding: utf-8 -*-

from yuantacat.spider.financial_analysis_spider import FinancialAnalysisQuarterlySpider
from yuantacat.spider.financial_analysis_spider import FinancialAnalysisYearlySpider

import unittest

class FinancialAnalysisSpiderTest(unittest.TestCase):
    def test_crawl_quarterly_2498(self):
        spider = FinancialAnalysisQuarterlySpider()
        param = { 'stock_symbol' : '2498' }
        spider.crawl(param)
        self.assertTrue(spider.is_crawled(param))

    def test_crawl_yearly_2498(self):
        spider = FinancialAnalysisYearlySpider()
        param = { 'stock_symbol' : '2498' }
        spider.crawl(param)
        self.assertTrue(spider.is_crawled(param))
