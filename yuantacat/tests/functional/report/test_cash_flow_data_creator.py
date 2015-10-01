#-*- coding: utf-8 -*-

from yuantacat.report.cash_flow_data_creator import CashFlowDataCreator

import unittest

class LiquidityDataCreatorTest(unittest.TestCase):
    def test_create_yearly_1101(self):
        creator = CashFlowDataCreator()
        creator.create({ 
            'stock_symbol' : '1101',
            'period' : 'Y', 
        })

    def test_create_quarterly_1101(self):
        creator = CashFlowDataCreator()
        creator.create({ 
            'stock_symbol' : '1101',
            'period' : 'Q', 
        })
