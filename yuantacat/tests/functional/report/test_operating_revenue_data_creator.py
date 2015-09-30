#-*- coding: utf-8 -*-

from yuantacat.report.operating_revenue_data_creator import OperatingRevenueDataCreator

import unittest

class OperatingRevenueDataCreatorTest(unittest.TestCase):
    def test_create_1101(self):
        creator = OperatingRevenueDataCreator()
        creator.create({ 'stock_symbol' : '1101' })
