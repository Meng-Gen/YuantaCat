#-*- coding: utf-8 -*-

from yuantacat.analyzer.liquidity_analyzer import LiquidityAnalyzer

import datetime
import unittest

class LiquidityAnalyzerTest(unittest.TestCase):
    def test_get_analysis_quarterly_1101(self):
        analyzer = LiquidityAnalyzer(stock_symbol='1101', period='Q')

        current_ratio = analyzer.get_current_ratio().get_map()
        self.assertAlmostEqual(current_ratio[datetime.date(2015, 6, 30)], 1.2114, places=4)
        self.assertAlmostEqual(current_ratio[datetime.date(2015, 3, 31)], 1.3290, places=4)

        quick_ratio = analyzer.get_quick_ratio().get_map()
        self.assertAlmostEqual(quick_ratio[datetime.date(2015, 6, 30)], 1.0425, places=4)
        self.assertAlmostEqual(quick_ratio[datetime.date(2015, 3, 31)], 1.1245, places=4)

        interest_protection_multiples = analyzer.get_interest_protection_multiples().get_map()
        self.assertAlmostEqual(interest_protection_multiples[datetime.date(2015, 6, 30)], 8.76, places=2)
        self.assertAlmostEqual(interest_protection_multiples[datetime.date(2015, 3, 31)], 4.05, places=2)

    def test_get_analysis_yearly_1101(self):
        analyzer = LiquidityAnalyzer(stock_symbol='1101', period='Y')

        current_ratio = analyzer.get_current_ratio().get_map()
        self.assertAlmostEqual(current_ratio[datetime.date(2014, 12, 31)], 1.4076, places=4)
        self.assertAlmostEqual(current_ratio[datetime.date(2013, 12, 31)], 1.2470, places=4)

        quick_ratio = analyzer.get_quick_ratio().get_map()
        self.assertAlmostEqual(quick_ratio[datetime.date(2014, 12, 31)], 1.1992, places=4)
        self.assertAlmostEqual(quick_ratio[datetime.date(2013, 12, 31)], 1.0515, places=4)

        interest_protection_multiples = analyzer.get_interest_protection_multiples().get_map()
        self.assertAlmostEqual(interest_protection_multiples[datetime.date(2014, 12, 31)], 12.12, places=2)
        self.assertAlmostEqual(interest_protection_multiples[datetime.date(2013, 12, 31)], 10.74, places=2)
