#-*- coding: utf-8 -*-

from yuantacat.analyzer.capital_structure_analyzer import CapitalStructureAnalyzer

import unittest

class CapitalStructureAnalyzerTest(unittest.TestCase):
    def test_get_analysis_quarterly_1101(self):
        analyzer = CapitalStructureAnalyzer(stock_symbol='1101', period='Q')
        liabilities_ratio = analyzer.get_liabilities_ratio()
        equity_ratio = analyzer.get_equity_ratio()
        equity_multiplier = analyzer.get_equity_multiplier()
        
        # Assets = Liabilities + Equity
        accounting_equation = liabilities_ratio + equity_ratio
        for stmt_date, value in accounting_equation.get():
            self.assertAlmostEqual(value, 1, places=2)

        # EquityMultiplier = 1 / EquityRatio
        inverse_equation = equity_ratio * equity_multiplier
        for stmt_date, value in inverse_equation.get():
            self.assertAlmostEqual(value, 1, places=2)

    def test_get_analysis_yearly_1101(self):
        analyzer = CapitalStructureAnalyzer(stock_symbol='1101', period='Y')
        liabilities_ratio = analyzer.get_liabilities_ratio()
        equity_ratio = analyzer.get_equity_ratio()
        equity_multiplier = analyzer.get_equity_multiplier()
        
        # Assets = Liabilities + Equity
        accounting_equation = liabilities_ratio + equity_ratio
        for stmt_date, value in accounting_equation.get():
            self.assertAlmostEqual(value, 1, places=2)

        # EquityMultiplier = 1 / EquityRatio
        inverse_equation = equity_ratio * equity_multiplier
        for stmt_date, value in inverse_equation.get():
            self.assertAlmostEqual(value, 1, places=2)
