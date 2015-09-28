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