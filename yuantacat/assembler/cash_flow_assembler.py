#-*- coding: utf-8 -*-

from yuantacat.dao.cash_flow_dao import CashFlowDao
from yuantacat.assembler.financial_statement_assembler import FinancialStatementAssembler

class CashFlowQuarterlyAssembler():
    def assemble(self, param):
        assembler = FinancialStatementAssembler('basic')
        dao = assembler.assemble(param)
        return CashFlowDao(dao['column_name_list'], dao['row_list'], dao['stock_symbol'], 'Q')

class CashFlowYearlyAssembler():
    def assemble(self, param):
        assembler = FinancialStatementAssembler('basic')
        dao = assembler.assemble(param)
        return CashFlowDao(dao['column_name_list'], dao['row_list'], dao['stock_symbol'], 'Y')
