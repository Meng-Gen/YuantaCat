#-*- coding: utf-8 -*-

from yuantacat.analyzer.operating_revenue_analyzer import OperatingRevenueAnalyzer

import datetime
import unittest

class OperatingRevenueAnalyzerTest(unittest.TestCase):
    def test_get_analysis_1101(self):
        analyzer = OperatingRevenueAnalyzer(stock_symbol='1101')
        operating_revenue = analyzer.get_operating_revenue().get_map()
        self.assertEqual(operating_revenue[datetime.date(2015, 8, 31)], 7397417)
        self.assertEqual(operating_revenue[datetime.date(2015, 7, 31)], 8250361)

        accumulated_operating_revenue = analyzer.get_accumulated_operating_revenue().get_map()
        self.assertEqual(accumulated_operating_revenue[datetime.date(2015, 8, 31)], 62092092)
        self.assertEqual(accumulated_operating_revenue[datetime.date(2015, 7, 31)], 54694675)

        accumulated_operating_revenue_yoy = analyzer.get_accumulated_operating_revenue_yoy().get_map()
        self.assertAlmostEqual(accumulated_operating_revenue_yoy[datetime.date(2015, 8, 31)], -0.2127, places=4)
        self.assertAlmostEqual(accumulated_operating_revenue_yoy[datetime.date(2015, 7, 31)], -0.2064, places=4)

        long_term_average = analyzer.get_long_term_average().get_map()
        self.assertAlmostEqual(long_term_average[datetime.date(2015, 8, 31)], 8462437, places=0)
        self.assertAlmostEqual(long_term_average[datetime.date(2015, 7, 31)], 8675246, places=0)

        short_term_average = analyzer.get_short_term_average().get_map()
        self.assertAlmostEqual(short_term_average[datetime.date(2015, 8, 31)], 8064544, places=0)
        self.assertAlmostEqual(short_term_average[datetime.date(2015, 7, 31)], 8262062, places=0)
