#-*- coding: utf-8 -*-

from yuantacat.report.dividend_policy_data_creator import DividendPolicyDataCreator

import unittest

class DividendPolicyDataCreatorTest(unittest.TestCase):
    def test_create_1101(self):
        creator = DividendPolicyDataCreator()
        creator.create({ 
            'stock_symbol' : '1101',
        })
