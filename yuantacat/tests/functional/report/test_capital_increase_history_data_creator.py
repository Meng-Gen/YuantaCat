#-*- coding: utf-8 -*-

from yuantacat.report.capital_increase_history_data_creator import CapitalIncreaseHistoryDataCreator

import datetime
import unittest

class CapitalIncreaseHistoryDataCreatorTest(unittest.TestCase):
    def test_create_1101(self):
        creator = CapitalIncreaseHistoryDataCreator()
        creator.create({ 'stock_symbol' : '1101' })
