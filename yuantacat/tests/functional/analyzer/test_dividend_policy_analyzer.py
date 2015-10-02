#-*- coding: utf-8 -*-

from yuantacat.analyzer.dividend_policy_analyzer import DividendPolicyAnalyzer

import datetime
import unittest

class CapitalIncreaseHistoryAnalyzerTest(unittest.TestCase):
    def test_get_capital_increase_1101(self):
        analyzer = DividendPolicyAnalyzer('1101')
        cash_dividends = analyzer.get_cash_dividends().get_map()
        self.assertEqual(cash_dividends[datetime.date(1993, 12, 31)], 2.0)
        self.assertEqual(cash_dividends[datetime.date(1994, 12, 31)], 1.0)
        self.assertEqual(cash_dividends[datetime.date(1997, 12, 31)], 0.5)

        stock_dividends = analyzer.get_stock_dividends().get_map()
        self.assertEqual(stock_dividends[datetime.date(1993, 12, 31)], 1.3)
        self.assertEqual(stock_dividends[datetime.date(1994, 12, 31)], 1.2)
        self.assertEqual(stock_dividends[datetime.date(1997, 12, 31)], 1.0)

        employee_stock_bonus_ratio = analyzer.get_employee_stock_bonus_ratio().get_map()
        self.assertEqual(employee_stock_bonus_ratio[datetime.date(1993, 12, 31)], 0.0)
        self.assertEqual(employee_stock_bonus_ratio[datetime.date(1994, 12, 31)], 0.0)
        self.assertEqual(employee_stock_bonus_ratio[datetime.date(1997, 12, 31)], 0.0)
