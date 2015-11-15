#-*- coding: utf-8 -*-

from yuantacat.report.kn_data_creator import KnDataCreator

import unittest

class KnDataCreatorTest(unittest.TestCase):
    def test_create_yearly_1101(self):
        creator = KnDataCreator()
        creator.create({ 
            'stock_symbol' : '1101',
            'period' : 'Y', 
        })

    def test_create_quarterly_1101(self):
        creator = KnDataCreator()
        creator.create({ 
            'stock_symbol' : '1101',
            'period' : 'Q', 
        })
