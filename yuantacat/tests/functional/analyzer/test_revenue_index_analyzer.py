#-*- coding: utf-8 -*-

from yuantacat.analyzer.revenue_index_analyzer import RevenueIndexAnalyzer

import datetime
import unittest

class RevenueIndexAnalyzerTest(unittest.TestCase):
    def test_get_analysis_1101(self):
        analyzer = RevenueIndexAnalyzer(stock_symbol='1101', period='Q')

        inventory_index = analyzer.get_inventory_index().get_map()
        self.assertTrue(inventory_index[datetime.date(2015, 6, 30)] < 0)
        self.assertTrue(inventory_index[datetime.date(2015, 3, 31)] > 0)

        accounts_receivable_index = analyzer.get_accounts_receivable_index().get_map()
        self.assertTrue(accounts_receivable_index[datetime.date(2015, 6, 30)] < 0)
        self.assertTrue(accounts_receivable_index[datetime.date(2015, 3, 31)] > 0)

        gross_profit_index = analyzer.get_gross_profit_index().get_map()
        self.assertTrue(gross_profit_index[datetime.date(2015, 6, 30)] > 0)
        self.assertTrue(gross_profit_index[datetime.date(2015, 3, 31)] > 0)

        selling_and_administrative_expenses_index \
                = analyzer.get_selling_and_administrative_expenses_index().get_map()
        self.assertTrue(selling_and_administrative_expenses_index[datetime.date(2015, 6, 30)] < 0)
        self.assertTrue(selling_and_administrative_expenses_index[datetime.date(2015, 3, 31)] > 0)

        accounts_payable_index = analyzer.get_accounts_payable_index().get_map()
        self.assertTrue(accounts_payable_index[datetime.date(2015, 6, 30)] < 0)
        self.assertTrue(accounts_payable_index[datetime.date(2015, 3, 31)] < 0)
