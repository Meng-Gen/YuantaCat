#-*- coding: utf-8 -*-

from yuantacat.report.capital_structure_data_creator import CapitalStructureDataCreator

import unittest

class CapitalStructureDataCreatorTest(unittest.TestCase):
    def test_create_1101(self):
        creator = CapitalStructureDataCreator()
        creator.create({ 
            'stock_symbol' : '1101',
            'period' : 'Y', 
        })
