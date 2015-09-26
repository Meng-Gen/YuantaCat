#-*- coding: utf-8 -*-

from yuantacat.analyzer.dupont_analyzer import DupontAnalyzer

import datetime
import unittest

class DupontAnalyzerTest(unittest.TestCase):
    def test_get_analysis_1101(self):
        analyzer = DupontAnalyzer(stock_symbol='1101', period='Q')
        #roe = analyzer.get_roe().get()
        #print roe
