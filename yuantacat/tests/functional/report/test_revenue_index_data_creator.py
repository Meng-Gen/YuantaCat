#-*- coding: utf-8 -*-

from yuantacat.report.revenue_index_data_creator import RevenueIndexDataCreator

import unittest

class RevenueIndexDataCreatorDataCreatorTest(unittest.TestCase):
    def test_create_yearly_1101(self):
        creator = RevenueIndexDataCreator()
        creator.create({ 
            'stock_symbol' : '1101',
            'period' : 'Y', 
        })

    def test_create_quarterly_1101(self):
        creator = RevenueIndexDataCreator()
        creator.create({ 
            'stock_symbol' : '1101',
            'period' : 'Q', 
        })
