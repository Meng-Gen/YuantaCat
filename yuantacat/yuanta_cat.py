#-*- coding: utf-8 -*-

from yuantacat.pipeline.stock_symbol_pipeline import StockSymbolPipeline
from yuantacat.pipeline.dividend_policy_pipeline import DividendPolicyPipeline
from yuantacat.pipeline.capital_increase_history_pipeline import CapitalIncreaseHistoryPipeline
from yuantacat.pipeline.profitability_pipeline import ProfitabilityPipeline

import logging

class YuantaCat():
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def run(self):
        #self.run_stock_symbol()
        #self.run_dividend_policy()
        #self.run_capital_increase_history()
        self.run_profitability()

    def run_stock_symbol(self):
        StockSymbolPipeline().run()

    def run_dividend_policy(self):
        DividendPolicyPipeline().run()

    def run_capital_increase_history(self):
        CapitalIncreaseHistoryPipeline().run()

    def run_profitability(self):
        ProfitabilityPipeline().run()
