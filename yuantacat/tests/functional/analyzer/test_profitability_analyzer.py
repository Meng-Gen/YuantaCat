#-*- coding: utf-8 -*-

from yuantacat.analyzer.profitability_analyzer import ProfitabilityAnalyzer

import datetime
import unittest

class ProfitabilityAnalyzerTest(unittest.TestCase):
    def test_get_analysis_1101(self):
        analyzer = ProfitabilityAnalyzer(stock_symbol='1101', period='Q')

        gross_profit_margin = analyzer.get_gross_profit_margin().get_map()
        self.assertAlmostEqual(gross_profit_margin[datetime.date(2015, 6, 30)], 0.1567, places=4)
        self.assertAlmostEqual(gross_profit_margin[datetime.date(2015, 3, 31)], 0.1334, places=4)

        operating_profit_margin = analyzer.get_operating_profit_margin().get_map()
        self.assertAlmostEqual(operating_profit_margin[datetime.date(2015, 6, 30)], 0.1167, places=4)
        self.assertAlmostEqual(operating_profit_margin[datetime.date(2015, 3, 31)], 0.0790, places=4)

        net_profit_before_tax_margin = analyzer.get_net_profit_before_tax_margin().get_map()
        self.assertAlmostEqual(net_profit_before_tax_margin[datetime.date(2015, 6, 30)], 0.1298, places=4)
        self.assertAlmostEqual(net_profit_before_tax_margin[datetime.date(2015, 3, 31)], 0.0686, places=4)

        net_profit_margin = analyzer.get_net_profit_margin().get_map()
        self.assertAlmostEqual(net_profit_margin[datetime.date(2015, 6, 30)], 0.1091, places=4)
        self.assertAlmostEqual(net_profit_margin[datetime.date(2015, 3, 31)], 0.0455, places=4)
