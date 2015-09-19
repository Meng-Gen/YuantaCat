#-*- coding: utf-8 -*-

from yuantacat.assembler.assemble_error import NoRecordAssembleError
from yuantacat.assembler.income_statement_assembler import IncomeStatementQuarterlyAssembler
from yuantacat.assembler.income_statement_assembler import IncomeStatementYearlyAssembler
from yuantacat.common.file_utils import FileUtils

import datetime
import unittest

class IncomeStatementAssemblerTest(unittest.TestCase):
    def test_assemble_quarterly_2498(self):
        # online: http://jdata.yuanta.com.tw/z/zc/zcq/zcq_2498.djhtm
        path = './yuantacat/tests/unit/data/income_statement_quarterly/2498.html'
        param = {
            'content' : FileUtils().read_file(path),
            'stock_symbol' : '2498'
        }
        dao = IncomeStatementQuarterlyAssembler().assemble(param)

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
        self.assertEqual(row_list[0], [u'營業收入淨額', 33010, 41524, 47866, 41864, 65060, 33121, 42900, 47048])
        for row in row_list:
            self.assertEqual(len(row), 9)
    
    def test_assemble_yearly_2498(self):
        # online: http://jdata.yuanta.com.tw/z/zc/zcq/zcqa_2498.djhtm
        path = './yuantacat/tests/unit/data/income_statement_yearly/2498.html'
        param = {
            'content' : FileUtils().read_file(path),
            'stock_symbol' : '2498'
        }
        dao = IncomeStatementYearlyAssembler().assemble(param)

        self.assertEqual(dao.get_stock_symbol(), param['stock_symbol'])

        actual = dao.get_column_name_list()
        expected = [
            u'年', 
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
        self.assertEqual(row_list[0], [u'營業收入淨額', 187911, 203403, 289020, 465795, 278761, 144493, 152353, 118218])
        for row in row_list:
            self.assertEqual(len(row), 9)
    
    def test_assemble_quarterly_raise_no_record_assemble_error(self):
        # online: http://jdata.yuanta.com.tw/z/zc/zcq/zcq_3009.djhtm
        path = './yuantacat/tests/unit/data/error/income_statement_quarterly_not_found_error.html'
        param = {
            'content' : FileUtils().read_file(path),
            'stock_symbol' : '3009'
        }
        with self.assertRaises(NoRecordAssembleError) as context:
            IncomeStatementQuarterlyAssembler().assemble(param)
        self.assertEqual(context.exception.param['stock_symbol'], param['stock_symbol'])   
    
    def test_assemble_yearly_raise_no_record_assemble_error(self):
        # online: http://jdata.yuanta.com.tw/z/zc/zcq/zcqa_3009.djhtm
        path = './yuantacat/tests/unit/data/error/income_statement_yearly_not_found_error.html'
        param = {
            'content' : FileUtils().read_file(path),
            'stock_symbol' : '3009'
        }
        with self.assertRaises(NoRecordAssembleError) as context:
            IncomeStatementYearlyAssembler().assemble(param)
        self.assertEqual(context.exception.param['stock_symbol'], param['stock_symbol'])   
    
    