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

        dio = analyzer.get_dio().get_map()
        self.assertAlmostEqual(dio[datetime.date(2015, 6, 30)], 42.8001, places=4)
        self.assertAlmostEqual(dio[datetime.date(2015, 3, 31)], 50.2123, places=4)

        dso = analyzer.get_dso().get_map()
        self.assertAlmostEqual(dso[datetime.date(2015, 6, 30)], 78.7038, places=4)
        self.assertAlmostEqual(dso[datetime.date(2015, 3, 31)], 102.7882, places=4)

        dpo = analyzer.get_dpo().get_map()
        self.assertAlmostEqual(dpo[datetime.date(2015, 6, 30)], 34.0699, places=4)
        self.assertAlmostEqual(dpo[datetime.date(2015, 3, 31)], 34.8615, places=4)

        cash_conversion_cycle = analyzer.get_cash_conversion_cycle().get_map()
        self.assertAlmostEqual(cash_conversion_cycle[datetime.date(2015, 6, 30)], 87.4339, places=4)
        self.assertAlmostEqual(cash_conversion_cycle[datetime.date(2015, 3, 31)], 118.1390, places=4)

        interest_protection_multiples = analyzer.get_interest_protection_multiples().get_map()
        self.assertAlmostEqual(interest_protection_multiples[datetime.date(2015, 6, 30)], 8.76, places=2)
        self.assertAlmostEqual(interest_protection_multiples[datetime.date(2015, 3, 31)], 4.05, places=2)

        roc = analyzer.get_roc().get_map()
        self.assertAlmostEqual(roc[datetime.date(2015, 6, 30)], 0.0150, places=4)
        self.assertAlmostEqual(roc[datetime.date(2015, 3, 31)], 0.0079, places=4)

    def test_get_analysis_yearly_1101(self):
        analyzer = LiquidityAnalyzer(stock_symbol='1101', period='Y')

        current_ratio = analyzer.get_current_ratio().get_map()
        self.assertAlmostEqual(current_ratio[datetime.date(2014, 12, 31)], 1.4076, places=4)
        self.assertAlmostEqual(current_ratio[datetime.date(2013, 12, 31)], 1.2470, places=4)

        quick_ratio = analyzer.get_quick_ratio().get_map()
        self.assertAlmostEqual(quick_ratio[datetime.date(2014, 12, 31)], 1.1992, places=4)
        self.assertAlmostEqual(quick_ratio[datetime.date(2013, 12, 31)], 1.0515, places=4)

        dio = analyzer.get_dio().get_map()
        self.assertAlmostEqual(dio[datetime.date(2014, 12, 31)], 38.5825, places=4)
        self.assertAlmostEqual(dio[datetime.date(2013, 12, 31)], 36.0163, places=4)

        dso = analyzer.get_dso().get_map()
        self.assertAlmostEqual(dso[datetime.date(2014, 12, 31)], 80.4196, places=4)
        self.assertAlmostEqual(dso[datetime.date(2013, 12, 31)], 70.4227, places=4)

        dpo = analyzer.get_dpo().get_map()
        self.assertAlmostEqual(dpo[datetime.date(2014, 12, 31)], 30.6520, places=4)
        self.assertAlmostEqual(dpo[datetime.date(2013, 12, 31)], 31.9076, places=4)

        cash_conversion_cycle = analyzer.get_cash_conversion_cycle().get_map()
        self.assertAlmostEqual(cash_conversion_cycle[datetime.date(2014, 12, 31)], 88.3502, places=4)
        self.assertAlmostEqual(cash_conversion_cycle[datetime.date(2013, 12, 31)], 74.5314, places=4)

        interest_protection_multiples = analyzer.get_interest_protection_multiples().get_map()
        self.assertAlmostEqual(interest_protection_multiples[datetime.date(2014, 12, 31)], 12.12, places=2)
        self.assertAlmostEqual(interest_protection_multiples[datetime.date(2013, 12, 31)], 10.74, places=2)

        roc = analyzer.get_roc().get_map()
        self.assertAlmostEqual(roc[datetime.date(2014, 12, 31)], 0.0935, places=4)
        self.assertAlmostEqual(roc[datetime.date(2013, 12, 31)], 0.0889, places=4)
