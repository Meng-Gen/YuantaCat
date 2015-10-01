#-*- coding: utf-8 -*-

from yuantacat.analyzer.capital_increase_history_analyzer import CapitalIncreaseHistoryAnalyzer

import datetime
import unittest

class CapitalIncreaseHistoryAnalyzerTest(unittest.TestCase):
    def test_get_capital_increase_1101(self):
        analyzer = CapitalIncreaseHistoryAnalyzer('1101')
        capital_increase = analyzer.get_capital_increase_by_cash().get_map()
        self.assertEqual(capital_increase[datetime.date(1993, 12, 31)], 53.00075)
        self.assertEqual(capital_increase[datetime.date(1994, 12, 31)], 53.00075)
        self.assertEqual(capital_increase[datetime.date(1997, 12, 31)], 63.0255)

        capital_increase = analyzer.get_capital_increase_by_earnings().get_map()
        self.assertEqual(capital_increase[datetime.date(1993, 12, 31)], 27.26106)
        self.assertEqual(capital_increase[datetime.date(1994, 12, 31)], 30.29706)
        self.assertEqual(capital_increase[datetime.date(1997, 12, 31)], 58.62075)

        capital_increase = analyzer.get_capital_increase_by_surplus().get_map()
        self.assertEqual(capital_increase[datetime.date(1993, 12, 31)], 20.93819)
        self.assertEqual(capital_increase[datetime.date(1994, 12, 31)], 31.05819)
        self.assertEqual(capital_increase[datetime.date(1997, 12, 31)], 43.35375)
