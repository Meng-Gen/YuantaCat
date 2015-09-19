#-*- coding: utf-8 -*-

from yuantacat.assembler.assemble_error import NoRecordAssembleError
from yuantacat.assembler.financial_analysis_assembler import FinancialAnalysisQuarterlyAssembler
from yuantacat.assembler.financial_analysis_assembler import FinancialAnalysisYearlyAssembler
from yuantacat.common.file_utils import FileUtils

import datetime
import unittest

class FinancialAnalysisAssemblerTest(unittest.TestCase):
    def test_assemble_quarterly_2498(self):
        # online: http://jdata.yuanta.com.tw/z/zc/zcr/zcr_2498.djhtm
        path = './yuantacat/tests/unit/data/financial_analysis_quarterly/2498.html'
        param = {
            'content' : FileUtils().read_file(path),
            'stock_symbol' : '2498'
        }
        dao = FinancialAnalysisQuarterlyAssembler().assemble(param)

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
        self.assertEqual(row_list[0], [u'獲利能力'])
        self.assertEqual(row_list[1], [u'營業毛利率', 19.27, 19.66, 20.36, 22.89, 22.23, 21.03, 17.8, 20.35])

    def test_assemble_yearly_2498(self):
        # online: http://jdata.yuanta.com.tw/z/zc/zcr/zcra_2498.djhtm
        path = './yuantacat/tests/unit/data/financial_analysis_yearly/2498.html'
        param = {
            'content' : FileUtils().read_file(path),
            'stock_symbol' : '2498'
        }
        dao = FinancialAnalysisYearlyAssembler().assemble(param)

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
        self.assertEqual(row_list[0], [u'淨值報酬率─稅後', 1.88, -1.68, 19.25, 70.34, 56.29, 35.79, 48.86, 58.48])
    
    def test_assemble_quarterly_raise_no_record_assemble_error(self):
        # online: http://jdata.yuanta.com.tw/z/zc/zcr/zcr_3009.djhtm
        path = './yuantacat/tests/unit/data/error/financial_analysis_quarterly_not_found_error.html'
        param = {
            'content' : FileUtils().read_file(path),
            'stock_symbol' : '3009'
        }
        with self.assertRaises(NoRecordAssembleError) as context:
            FinancialAnalysisQuarterlyAssembler().assemble(param)
        self.assertEqual(context.exception.param['stock_symbol'], param['stock_symbol'])   
    
    def test_assemble_yearly_raise_no_record_assemble_error(self):
        # online: http://jdata.yuanta.com.tw/z/zc/zcr/zcra_3009.djhtm
        path = './yuantacat/tests/unit/data/error/financial_analysis_yearly_not_found_error.html'
        param = {
            'content' : FileUtils().read_file(path),
            'stock_symbol' : '3009'
        }
        with self.assertRaises(NoRecordAssembleError) as context:
            FinancialAnalysisYearlyAssembler().assemble(param)
        self.assertEqual(context.exception.param['stock_symbol'], param['stock_symbol'])   
    
    