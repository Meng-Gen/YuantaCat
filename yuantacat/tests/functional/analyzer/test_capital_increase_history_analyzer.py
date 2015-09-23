#-*- coding: utf-8 -*-

from yuantacat.analyzer.capital_increase_history_analyzer import CapitalIncreaseHistoryAnalyzer

import datetime
import unittest

class CapitalIncreaseHistoryAnalyzerTest(unittest.TestCase):
    def setUp(self):
        self.analyzer = CapitalIncreaseHistoryAnalyzer()

    def tearDown(self):
        self.analyzer = None
    
    def test_get_capital_increase_by_cash_of_1101(self):
        capital_increase = self.analyzer.get_capital_increase_by_cash('1101')
        self.assertEqual(capital_increase[0], ('1101', datetime.date(1993, 12, 31), 53.00075))
        self.assertEqual(capital_increase[1], ('1101', datetime.date(1994, 12, 31), 53.00075))
        self.assertEqual(capital_increase[4], ('1101', datetime.date(1997, 12, 31), 63.0255))

    def test_get_capital_increase_by_earnings_of_1101(self):
        capital_increase = self.analyzer.get_capital_increase_by_earnings('1101')
        self.assertEqual(capital_increase[0], ('1101', datetime.date(1993, 12, 31), 27.26106))
        self.assertEqual(capital_increase[1], ('1101', datetime.date(1994, 12, 31), 30.29706))
        self.assertEqual(capital_increase[4], ('1101', datetime.date(1997, 12, 31), 58.62075))

    def test_get_capital_increase_by_surplus_of_1101(self):
        capital_increase = self.analyzer.get_capital_increase_by_surplus('1101')
        self.assertEqual(capital_increase[0], ('1101', datetime.date(1993, 12, 31), 20.93819))
        self.assertEqual(capital_increase[1], ('1101', datetime.date(1994, 12, 31), 31.05819))
        self.assertEqual(capital_increase[4], ('1101', datetime.date(1997, 12, 31), 43.35375))
