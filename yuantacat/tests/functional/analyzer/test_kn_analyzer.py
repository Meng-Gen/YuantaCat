#-*- coding: utf-8 -*-

from yuantacat.analyzer.kn_analyzer import KnAnalyzer

import datetime
import unittest

class KnAnalyzerTest(unittest.TestCase):
    def test_get_analysis_quarterly_1101(self):
        analyzer = KnAnalyzer(stock_symbol='1101', period='Q')
        max_kn = analyzer.get_max_kn().get_map()
        self.assertAlmostEqual(max_kn[datetime.date(2015, 6, 30)], 0.0547, places=4)
        self.assertAlmostEqual(max_kn[datetime.date(2015, 3, 31)], 0.0189, places=4)

        min_kn = analyzer.get_min_kn().get_map()
        self.assertAlmostEqual(min_kn[datetime.date(2015, 6, 30)], 0.0459, places=4)
        self.assertAlmostEqual(min_kn[datetime.date(2015, 3, 31)], 0.0175, places=4)

    def test_get_analysis_yearly_1101(self):
        analyzer = KnAnalyzer(stock_symbol='1101', period='Y')
        max_kn = analyzer.get_max_kn().get_map()
        self.assertAlmostEqual(max_kn[datetime.date(2014, 12, 31)], 0.0808, places=4)
        self.assertAlmostEqual(max_kn[datetime.date(2013, 12, 31)], 0.0962, places=4)

        min_kn = analyzer.get_min_kn().get_map()
        self.assertAlmostEqual(min_kn[datetime.date(2014, 12, 31)], 0.0678, places=4)
        self.assertAlmostEqual(min_kn[datetime.date(2013, 12, 31)], 0.0693, places=4)
