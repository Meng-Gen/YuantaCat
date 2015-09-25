#-*- coding: utf-8 -*-

from yuantacat.analyzer.liquidity_measurement_analyzer import LiquidityMeasurementAnalyzer

import datetime
import unittest

class LiquidityMeasurementAnalyzerTest(unittest.TestCase):
    def test_get_analysis_quarterly_1101(self):
        analyzer = LiquidityMeasurementAnalyzer(stock_symbol='1101', period='Q')
        current_ratio = analyzer.get_current_ratio().get_map()
        self.assertAlmostEqual(current_ratio[datetime.date(2015, 6, 30)], 1.2114, places=4)
        self.assertAlmostEqual(current_ratio[datetime.date(2015, 3, 31)], 1.3290, places=4)

        quick_ratio = analyzer.get_quick_ratio()
        print quick_ratio.get()

    def test_get_analysis_yearly_1101(self):
        analyzer = LiquidityMeasurementAnalyzer(stock_symbol='1101', period='Y')

