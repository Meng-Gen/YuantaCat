#-*- coding: utf-8 -*-

from yuantacat.assembler.assemble_error import NoRecordAssembleError
from yuantacat.assembler.operating_revenue_assembler import OperatingRevenueAssembler
from yuantacat.common.file_utils import FileUtils

import datetime
import unittest

class OperatingRevenueAssemblerTest(unittest.TestCase):
    def setUp(self):
        self.assembler = OperatingRevenueAssembler()
        self.file_utils = FileUtils()

    def tearDown(self):
        self.assembler = None
        self.file_utils = None
    
    def test_assemble_2498(self):
        # online: http://jdata.yuanta.com.tw/z/zc/zch/zch_2498.djhtm
        path = './yuantacat/tests/unit/data/operating_revenue/2498.html'
        param = {
            'content' : self.file_utils.read_file(path),
            'stock_symbol' : '2498'
        }
        dao = self.assembler.assemble(param)

        self.assertEqual(dao.get_stock_symbol(), param['stock_symbol'])

        actual = dao.get_column_name_list()
        expected = [u'年/月', u'合併營收', u'月增率', u'去年同期', u'年增率', u'累計營收', u'年增率']
        self.assertEqual(actual, expected)

        row_list = dao.get_row_list()
        self.assertEqual(row_list[0], [datetime.date(2015, 8, 31), 6889966, -0.0699, 14541044, -0.5262, 88831474, -0.2797])
        for row in row_list:
            self.assertEqual(len(row), 7)
    
    def test_assemble_raise_no_record_assemble_error(self):
        # online: http://jdata.yuanta.com.tw/z/zc/zch/zch_3009.djhtm
        path = './yuantacat/tests/unit/data/error/operating_revenue_not_found_error.html'
        param = {
            'content' : self.file_utils.read_file(path),
            'stock_symbol' : '3009'
        }
        with self.assertRaises(NoRecordAssembleError) as context:
            self.assembler.assemble(param)
        self.assertEqual(context.exception.param['stock_symbol'], param['stock_symbol'])   
    