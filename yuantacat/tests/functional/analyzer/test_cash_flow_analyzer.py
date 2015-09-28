#-*- coding: utf-8 -*-

from yuantacat.analyzer.cash_flow_analyzer import CashFlowAnalyzer

import datetime
import unittest

class CashFlowAnalyzerTest(unittest.TestCase):
    def test_get_analysis_quarterly_1101(self):
        analyzer = CashFlowAnalyzer(stock_symbol='1101', period='Q')
        net_profit = analyzer.get_net_profit().get_map()
        self.assertEqual(net_profit[datetime.date(2015, 6, 30)], 2728)
        self.assertEqual(net_profit[datetime.date(2015, 3, 31)], 975)

        cash_flow = analyzer.get_cash_flow_from_operating_activities().get_map()
        self.assertEqual(cash_flow[datetime.date(2015, 6, 30)], 5575)
        self.assertEqual(cash_flow[datetime.date(2015, 3, 31)], 5654)

        cash_flow = analyzer.get_cash_flow_from_investing_activities().get_map()
        self.assertEqual(cash_flow[datetime.date(2015, 6, 30)], -4712)
        self.assertEqual(cash_flow[datetime.date(2015, 3, 31)], -1500)

        cash_flow = analyzer.get_cash_flow_from_financing_activities().get_map()
        self.assertEqual(cash_flow[datetime.date(2015, 6, 30)], 4424)
        self.assertEqual(cash_flow[datetime.date(2015, 3, 31)], -3245)
        
        cash_flow = analyzer.get_free_cash_flow().get_map()
        self.assertEqual(cash_flow[datetime.date(2015, 6, 30)], 5575 - 4712)
        self.assertEqual(cash_flow[datetime.date(2015, 3, 31)], 5654 - 1500)

        cash_flow = analyzer.get_free_cash_flow().get_map()
        self.assertEqual(cash_flow[datetime.date(2015, 6, 30)], 5575 - 4712)
        self.assertEqual(cash_flow[datetime.date(2015, 3, 31)], 5654 - 1500)

        ratio = analyzer.get_long_term_investments_to_assets_ratio().get_map()
        self.assertAlmostEqual(ratio[datetime.date(2015, 6, 30)], 0.0648, places=4)
        self.assertAlmostEqual(ratio[datetime.date(2015, 3, 31)], 0.0695, places=4)

    def test_get_analysis_yearly_1101(self):
        analyzer = CashFlowAnalyzer(stock_symbol='1101', period='Y')
        net_profit = analyzer.get_net_profit().get_map()
        self.assertEqual(net_profit[datetime.date(2014, 12, 31)], 16584)
        self.assertEqual(net_profit[datetime.date(2013, 12, 31)], 15119)

        cash_flow = analyzer.get_cash_flow_from_operating_activities().get_map()
        self.assertEqual(cash_flow[datetime.date(2014, 12, 31)], 19987)
        self.assertEqual(cash_flow[datetime.date(2013, 12, 31)], 21974)

        cash_flow = analyzer.get_cash_flow_from_investing_activities().get_map()
        self.assertEqual(cash_flow[datetime.date(2014, 12, 31)], -3098)
        self.assertEqual(cash_flow[datetime.date(2013, 12, 31)], -1249)

        cash_flow = analyzer.get_cash_flow_from_financing_activities().get_map()
        self.assertEqual(cash_flow[datetime.date(2014, 12, 31)], -11731)
        self.assertEqual(cash_flow[datetime.date(2013, 12, 31)], -20773)
        
        cash_flow = analyzer.get_free_cash_flow().get_map()
        self.assertEqual(cash_flow[datetime.date(2014, 12, 31)], 19987 - 3098)
        self.assertEqual(cash_flow[datetime.date(2013, 12, 31)], 21974 - 1249)
        
        ratio = analyzer.get_long_term_investments_to_assets_ratio().get_map()
        self.assertAlmostEqual(ratio[datetime.date(2014, 12, 31)], 0.0730, places=4)
        self.assertAlmostEqual(ratio[datetime.date(2013, 12, 31)], 0.0679, places=4)
