#-*- coding: utf-8 -*-

from yuantacat.report.liquidity_data_creator import LiquidityDataCreator

import unittest

class LiquidityDataCreatorTest(unittest.TestCase):
    def test_create_yearly_1101(self):
        creator = LiquidityDataCreator()
        creator.create({ 
            'stock_symbol' : '1101',
            'period' : 'Y', 
        })

    def test_create_quarterly_1101(self):
        creator = LiquidityDataCreator()
        creator.create({ 
            'stock_symbol' : '1101',
            'period' : 'Q', 
        })
