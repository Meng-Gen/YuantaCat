#-*- coding: utf-8 -*-

from yuantacat.dao.financial_analysis_dao import FinancialAnalysisDao
from yuantacat.assembler.financial_statement_assembler import FinancialStatementAssembler

class FinancialAnalysisQuarterlyAssembler():
    def assemble(self, param):
        assembler = FinancialStatementAssembler('basic')
        dao = assembler.assemble(param)
        return FinancialAnalysisDao(dao['column_name_list'], dao['row_list'], dao['stock_symbol'])

class FinancialAnalysisYearlyAssembler():
    def assemble(self, param):
        assembler = FinancialStatementAssembler('form', column_name_pos=2)
        dao = assembler.assemble(param)
        return FinancialAnalysisDao(dao['column_name_list'], dao['row_list'], dao['stock_symbol'])
