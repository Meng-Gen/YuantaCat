#-*- coding: utf-8 -*-

from yuantacat.report.profitability_data_creator import ProfitabilityDataCreator

import unittest

class ProfitabilityDataCreatorTest(unittest.TestCase):
    def test_create_yearly_1101(self):
        creator = ProfitabilityDataCreator()
        creator.create({ 
            'stock_symbol' : '1101',
            'period' : 'Y', 
        })
