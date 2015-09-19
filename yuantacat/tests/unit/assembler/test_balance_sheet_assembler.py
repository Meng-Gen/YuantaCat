#-*- coding: utf-8 -*-

from yuantacat.assembler.assemble_error import NoRecordAssembleError
from yuantacat.assembler.balance_sheet_assembler import BalanceSheetQuarterlyAssembler
from yuantacat.assembler.balance_sheet_assembler import BalanceSheetYearlyAssembler
from yuantacat.common.file_utils import FileUtils

import datetime
import unittest

class BalanceSheetAssemblerTest(unittest.TestCase):
    def test_assemble_quarterly_2498(self):
        # online: http://jdata.yuanta.com.tw/z/zc/zcp/zcpa_2498.djhtm
        path = './yuantacat/tests/unit/data/balance_sheet_quarterly/2498.html'
        param = {
            'content' : FileUtils().read_file(path),
            'stock_symbol' : '2498'
        }
        dao = BalanceSheetQuarterlyAssembler().assemble(param)

        self.assertEqual(dao.get_stock_symbol(), param['stock_symbol'])

        actual = dao.get_column_name_list()
        expected = [
            u'期別', 
            datetime.date(2015, 6, 30), 
            datetime.date(2015, 3, 31), 
            datetime.date(2014, 12, 31),
            datetime.date(2014, 9, 30),
            datetime.date(2014, 6, 30),
            datetime.date(2014, 3, 31),
            datetime.date(2013, 12, 31),
            datetime.date(2013, 9, 30)
        ]
        self.assertEqual(actual, expected)

        row_list = dao.get_row_list()
        self.assertEqual(row_list[0], [u'現金及約當現金', 47233, 51715, 55744, 54672, 48438, 43930, 53299, 43120])
        for row in row_list:
            self.assertEqual(len(row), 9)
    
    def test_assemble_yearly_2498(self):
        # online: http://jdata.yuanta.com.tw/z/zc/zcp/zcpb_2498.djhtm
        path = './yuantacat/tests/unit/data/balance_sheet_yearly/2498.html'
        param = {
            'content' : FileUtils().read_file(path),
            'stock_symbol' : '2498'
        }
        dao = BalanceSheetYearlyAssembler().assemble(param)

        self.assertEqual(dao.get_stock_symbol(), param['stock_symbol'])

        actual = dao.get_column_name_list()
        expected = [
            u'期別', 
            datetime.date(2014, 12, 31),
            datetime.date(2013, 12, 31),
            datetime.date(2012, 12, 31),
            datetime.date(2011, 12, 31),
            datetime.date(2010, 12, 31),
            datetime.date(2009, 12, 31),
            datetime.date(2008, 12, 31),
            datetime.date(2007, 12, 31)
        ]
        self.assertEqual(actual, expected)

        row_list = dao.get_row_list()
        self.assertEqual(row_list[0], [u'現金及約當現金', 55744, 53299, 53878, 87502, 74463, 64638, 64238, 56490])
        for row in row_list:
            self.assertEqual(len(row), 9)
    
    def test_assemble_quarterly_raise_no_record_assemble_error(self):
        # online: http://jdata.yuanta.com.tw/z/zc/zcpa/zcpa_3009.djhtm
        path = './yuantacat/tests/unit/data/error/balance_sheet_quarterly_not_found_error.html'
        param = {
            'content' : FileUtils().read_file(path),
            'stock_symbol' : '3009'
        }
        with self.assertRaises(NoRecordAssembleError) as context:
            BalanceSheetQuarterlyAssembler().assemble(param)
        self.assertEqual(context.exception.param['stock_symbol'], param['stock_symbol'])   
    
    def test_assemble_yearly_raise_no_record_assemble_error(self):
        # online: http://jdata.yuanta.com.tw/z/zc/zcpb/zcpb_3009.djhtm
        path = './yuantacat/tests/unit/data/error/balance_sheet_yearly_not_found_error.html'
        param = {
            'content' : FileUtils().read_file(path),
            'stock_symbol' : '3009'
        }
        with self.assertRaises(NoRecordAssembleError) as context:
            BalanceSheetQuarterlyAssembler().assemble(param)
        self.assertEqual(context.exception.param['stock_symbol'], param['stock_symbol'])   
    
    