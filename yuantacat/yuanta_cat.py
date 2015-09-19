#-*- coding: utf-8 -*-

from yuantacat.pipeline.stock_symbol_pipeline import StockSymbolPipeline
from yuantacat.pipeline.dividend_policy_pipeline import DividendPolicyPipeline
from yuantacat.pipeline.capital_increase_history_pipeline import CapitalIncreaseHistoryPipeline
from yuantacat.pipeline.profitability_pipeline import ProfitabilityPipeline
from yuantacat.pipeline.operating_revenue_pipeline import OperatingRevenuePipeline
from yuantacat.pipeline.balance_sheet_pipeline import BalanceSheetQuarterlyPipeline
from yuantacat.pipeline.balance_sheet_pipeline import BalanceSheetYearlyPipeline
from yuantacat.pipeline.income_statement_pipeline import IncomeStatementQuarterlyPipeline
from yuantacat.pipeline.income_statement_pipeline import IncomeStatementYearlyPipeline
from yuantacat.pipeline.cash_flow_pipeline import CashFlowQuarterlyPipeline
from yuantacat.pipeline.cash_flow_pipeline import CashFlowYearlyPipeline
from yuantacat.pipeline.financial_analysis_pipeline import FinancialAnalysisQuarterlyPipeline
from yuantacat.pipeline.financial_analysis_pipeline import FinancialAnalysisYearlyPipeline

import logging

class YuantaCat():
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def run(self):
        #self.run_stock_symbol()
        #self.run_dividend_policy()
        #self.run_capital_increase_history()
        #self.run_profitability()
        #self.run_operating_revenue()
        #self.run_balance_sheet()
        #self.run_income_statement()
        #self.run_cash_flow()
        self.run_financial_analysis()

    def run_stock_symbol(self):
        StockSymbolPipeline().run()

    def run_dividend_policy(self):
        DividendPolicyPipeline().run()

    def run_capital_increase_history(self):
        CapitalIncreaseHistoryPipeline().run()

    def run_profitability(self):
        ProfitabilityPipeline().run()

    def run_operating_revenue(self):
        OperatingRevenuePipeline().run()

    def run_balance_sheet(self):
        BalanceSheetQuarterlyPipeline().run()
        BalanceSheetYearlyPipeline().run()

    def run_income_statement(self):
        IncomeStatementQuarterlyPipeline().run()
        IncomeStatementYearlyPipeline().run()

    def run_cash_flow(self):
        CashFlowQuarterlyPipeline().run()
        CashFlowYearlyPipeline().run()

    def run_financial_analysis(self):
        FinancialAnalysisQuarterlyPipeline().run()
        FinancialAnalysisYearlyPipeline().run()
