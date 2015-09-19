#-*- coding: utf-8 -*-

from yuantacat.assembler.assemble_error import NoRecordAssembleError
from yuantacat.assembler.cash_flow_assembler import CashFlowQuarterlyAssembler
from yuantacat.assembler.cash_flow_assembler import CashFlowYearlyAssembler
from yuantacat.common.file_utils import FileUtils

import datetime
import unittest

class CashFlowAssemblerTest(unittest.TestCase):
    def test_assemble_quarterly_2498(self):
        # online: http://jdata.yuanta.com.tw/z/zc/zc3/zc3_2498.djhtm
        path = './yuantacat/tests/unit/data/cash_flow_quarterly/2498.html'
        param = {
            'content' : FileUtils().read_file(path),
            'stock_symbol' : '2498'
        }
        dao = CashFlowQuarterlyAssembler().assemble(param)

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
        self.assertEqual(row_list[0], [u'稅後淨利', -8034, 360, 466, 641, 2257, -1881, 315, -2974])
        for row in row_list[:-1]:
            self.assertEqual(len(row), 9)
        self.assertEqual(row_list[-1], [u'[說明]上列會計科目中，投資收益－權益法、長期投資(新增)、固定資產(購置)、'])
    
    def test_assemble_yearly_2498(self):
        # online: http://jdata.yuanta.com.tw/z/zc/zc3/zc3a_2498.djhtm
        path = './yuantacat/tests/unit/data/cash_flow_yearly/2498.html'
        param = {
            'content' : FileUtils().read_file(path),
            'stock_symbol' : '2498'
        }
        dao = CashFlowYearlyAssembler().assemble(param)

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
        self.assertEqual(row_list[0], [u'稅後淨利', 1483, -1324, 17589, 62299, 39515, 22614, 28553, 28918])
        for row in row_list[:-1]:
            self.assertEqual(len(row), 9)
        self.assertEqual(row_list[-1], [u'[說明]上列會計科目中，投資收益－權益法、長期投資(新增)、固定資產(購置)、'])
    
    def test_assemble_quarterly_raise_no_record_assemble_error(self):
        # online: http://jdata.yuanta.com.tw/z/zc/zc3/zc3_3009.djhtm
        path = './yuantacat/tests/unit/data/error/income_statement_quarterly_not_found_error.html'
        param = {
            'content' : FileUtils().read_file(path),
            'stock_symbol' : '3009'
        }
        with self.assertRaises(NoRecordAssembleError) as context:
            CashFlowQuarterlyAssembler().assemble(param)
        self.assertEqual(context.exception.param['stock_symbol'], param['stock_symbol'])   
    
    def test_assemble_yearly_raise_no_record_assemble_error(self):
        # online: http://jdata.yuanta.com.tw/z/zc/zc3/zc3a_3009.djhtm
        path = './yuantacat/tests/unit/data/error/income_statement_yearly_not_found_error.html'
        param = {
            'content' : FileUtils().read_file(path),
            'stock_symbol' : '3009'
        }
        with self.assertRaises(NoRecordAssembleError) as context:
            CashFlowYearlyAssembler().assemble(param)
        self.assertEqual(context.exception.param['stock_symbol'], param['stock_symbol'])   
    
    