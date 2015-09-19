#-*- coding: utf-8 -*-

from yuantacat.assembler.assemble_error import NoRecordAssembleError
from yuantacat.assembler.profitability_assembler import ProfitabilityAssembler
from yuantacat.common.file_utils import FileUtils

import datetime
import unittest

class ProfitabilityAssemblerTest(unittest.TestCase):
    def test_assemble_2498(self):
        # online: http://jdata.yuanta.com.tw/z/zc/zce/zce_2498.djhtm
        path = './yuantacat/tests/unit/data/profitability/2498.html'
        param = {
            'content' : FileUtils().read_file(path),
            'stock_symbol' : '2498'
        }
        dao = ProfitabilityAssembler().assemble(param)

        self.assertEqual(dao.get_stock_symbol(), param['stock_symbol'])

        actual = dao.get_column_name_list()
        expected = [u'季別', u'營業收入', u'營業成本', u'營業毛利', u'毛利率', u'營業利益', u'營益率', u'業外收支', u'稅前淨利', u'稅後淨利']
        self.assertEqual(actual, expected)

        row_list = dao.get_row_list()
        self.assertEqual(row_list[0], [datetime.date(2015, 6, 30), 33010, 26648, 6362, 0.1927, -5141, -0.1557, -2777, -7918, -8034])
        for row in row_list:
            self.assertEqual(len(row), 10)
    
    def test_assemble_raise_no_record_assemble_error(self):
        # online: http://jdata.yuanta.com.tw/z/zc/zce/zce_3009.djhtm
        path = './yuantacat/tests/unit/data/error/profitability_not_found_error.html'
        param = {
            'content' : FileUtils().read_file(path),
            'stock_symbol' : '3009'
        }
        with self.assertRaises(NoRecordAssembleError) as context:
            ProfitabilityAssembler().assemble(param)
        self.assertEqual(context.exception.param['stock_symbol'], param['stock_symbol'])   
