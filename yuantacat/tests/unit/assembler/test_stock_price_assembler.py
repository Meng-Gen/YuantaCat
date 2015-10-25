#-*- coding: utf-8 -*-

from yuantacat.assembler.stock_price_assembler import StockPriceAssembler
from yuantacat.common.file_utils import FileUtils

import datetime
import unittest

class StockPriceAssemblerTest(unittest.TestCase):
    def test_assemble_2498(self):
        # online:  http://real-chart.finance.yahoo.com/table.csv?s=2498.TW&ignore=.csv
        path = './yuantacat/tests/unit/data/stock_price/2498.html'
        param = {
            'content' : FileUtils().read_file(path),
            'stock_symbol' : '2498'
        }
        dao = StockPriceAssembler().assemble(param)
        self.assertEqual(dao.get_stock_symbol(), param['stock_symbol'])

        actual = dao.get_column_name_list()
        expected = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Adj Close']
        self.assertEqual(actual, expected)

        row_list = dao.get_row_list()
        self.assertEqual(row_list[0], [datetime.date(2015, 10, 23), 80.9, 81.3, 76.8, 77.0, 23948000, 77.0])
        for row in row_list:
            self.assertEqual(len(row), 7)  
