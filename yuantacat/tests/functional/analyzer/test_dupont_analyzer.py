#-*- coding: utf-8 -*-

from yuantacat.analyzer.dupont_analyzer import DupontAnalyzer

import datetime
import unittest

class DupontAnalyzerTest(unittest.TestCase):
    def test_get_analysis_1101(self):
        analyzer = DupontAnalyzer(stock_symbol='1101', period='Q')
        roe = analyzer.get_roe().get_map()
        self.assertAlmostEqual(roe[datetime.date(2015, 6, 30)], 0.0174, places=4)
        self.assertAlmostEqual(roe[datetime.date(2015, 3, 31)], 0.0060, places=4)

        roa = analyzer.get_roa().get_map()
        self.assertAlmostEqual(roa[datetime.date(2015, 6, 30)], 0.0093, places=4)
        self.assertAlmostEqual(roa[datetime.date(2015, 3, 31)], 0.0033, places=4)

        ros = analyzer.get_ros().get_map()
        self.assertAlmostEqual(ros[datetime.date(2015, 6, 30)], 0.1091, places=4)
        self.assertAlmostEqual(ros[datetime.date(2015, 3, 31)], 0.0455, places=4)

        ato = analyzer.get_ato().get_map()
        self.assertAlmostEqual(ato[datetime.date(2015, 6, 30)], 0.0848, places=4)
        self.assertAlmostEqual(ato[datetime.date(2015, 3, 31)], 0.0736, places=4)

        equity_multiplier = analyzer.get_equity_multiplier().get_map()
        self.assertAlmostEqual(equity_multiplier[datetime.date(2015, 6, 30)], 1.8828, places=4)
        self.assertAlmostEqual(equity_multiplier[datetime.date(2015, 3, 31)], 1.7966, places=4)
