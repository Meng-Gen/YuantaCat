#-*- coding: utf-8 -*-

from yuantacat.dao.income_statement_dao import IncomeStatementDao
from yuantacat.assembler.financial_statement_assembler import FinancialStatementAssembler

class IncomeStatementQuarterlyAssembler():
    def assemble(self, param):
        assembler = FinancialStatementAssembler('basic')
        dao = assembler.assemble(param)
        return IncomeStatementDao(dao['column_name_list'], dao['row_list'], dao['stock_symbol'], 'Q')

class IncomeStatementYearlyAssembler():
    def assemble(self, param):
        assembler = FinancialStatementAssembler('form')
        dao = assembler.assemble(param)
        return IncomeStatementDao(dao['column_name_list'], dao['row_list'], dao['stock_symbol'], 'Y')
