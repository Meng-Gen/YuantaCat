#-*- coding: utf-8 -*-

from yuantacat.assembler.assemble_error import NoRecordAssembleError
from yuantacat.assembler.balance_sheet_summary_assembler import BalanceSheetQuarterlySummaryAssembler
from yuantacat.assembler.balance_sheet_summary_assembler import BalanceSheetYearlySummaryAssembler
from yuantacat.common.file_utils import FileUtils

import datetime
import unittest

class BalanceSheetSummaryAssemblerTest(unittest.TestCase):
    def test_assemble_quarterly_2498(self):
        # online: http://jdata.yuanta.com.tw/z/zc/zcp/zcp_2498.djhtm
        path = './yuantacat/tests/unit/data/balance_sheet_summary/2498.html'
        param = {
            'content' : FileUtils().read_file(path),
            'stock_symbol' : '2498'
        }
        dao = BalanceSheetQuarterlySummaryAssembler().assemble(param)

        self.assertEqual(dao.get_stock_symbol(), param['stock_symbol'])

        self.assertEqual(dao.get_period(), 'Q')

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
        self.assertEqual(row_list[0], [u'流動資產', 105701, 114095, 110287, 110883, 122386, 103908, 111507, 112025])
        for row in row_list:
            self.assertEqual(len(row), 9)
    
    def test_assemble_yearly_2498(self):
        # online: http://jdata.yuanta.com.tw/z/zc/zcp/zcp_2498.djhtm
        path = './yuantacat/tests/unit/data/balance_sheet_summary/2498.html'
        param = {
            'content' : FileUtils().read_file(path),
            'stock_symbol' : '2498'
        }
        dao = BalanceSheetYearlySummaryAssembler().assemble(param)

        self.assertEqual(dao.get_stock_symbol(), param['stock_symbol'])

        self.assertEqual(dao.get_period(), 'Y')

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
        self.assertEqual(row_list[0], [u'流動資產', 110287, 111507, 139659, 192860, 168606, 104901, 104257, 85729])
        for row in row_list:
            self.assertEqual(len(row), 9)

    def test_assemble_raise_no_record_assemble_error(self):
        # online: http://jdata.yuanta.com.tw/z/zc/zcp/zcp_3009.djhtm
        path = './yuantacat/tests/unit/data/error/balance_sheet_summary_not_found_error.html'
        param = {
            'content' : FileUtils().read_file(path),
            'stock_symbol' : '3009'
        }
        with self.assertRaises(NoRecordAssembleError) as context:
            BalanceSheetQuarterlySummaryAssembler().assemble(param)
        self.assertEqual(context.exception.param['stock_symbol'], param['stock_symbol'])   
    