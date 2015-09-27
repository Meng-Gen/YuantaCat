#-*- coding: utf-8 -*-

from yuantacat.analyzer.capital_structure_analyzer import CapitalStructureAnalyzer

import datetime
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

        true_liabilities_ratio = analyzer.get_true_liabilities_ratio().get_map()
        self.assertAlmostEqual(true_liabilities_ratio[datetime.date(2015, 6, 30)], 0.2622, places=4)
        self.assertAlmostEqual(true_liabilities_ratio[datetime.date(2015, 3, 31)], 0.2104, places=4)

        long_term_capital_to_fixed_assets_ratio = analyzer.get_long_term_capital_to_fixed_assets_ratio().get_map()
        self.assertAlmostEqual(long_term_capital_to_fixed_assets_ratio[datetime.date(2015, 6, 30)], 1.80, places=2)
        self.assertAlmostEqual(long_term_capital_to_fixed_assets_ratio[datetime.date(2015, 3, 31)], 1.88, places=2)

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

        true_liabilities_ratio = analyzer.get_true_liabilities_ratio().get_map()
        self.assertAlmostEqual(true_liabilities_ratio[datetime.date(2014, 12, 31)], 0.2251, places=4)
        self.assertAlmostEqual(true_liabilities_ratio[datetime.date(2013, 12, 31)], 0.2230, places=4)

        long_term_capital_to_fixed_assets_ratio = analyzer.get_long_term_capital_to_fixed_assets_ratio().get_map()
        self.assertAlmostEqual(long_term_capital_to_fixed_assets_ratio[datetime.date(2014, 12, 31)], 1.96, places=2)
        self.assertAlmostEqual(long_term_capital_to_fixed_assets_ratio[datetime.date(2013, 12, 31)], 1.84, places=2)
