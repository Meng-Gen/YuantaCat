#-*- coding: utf-8 -*-

from yuantacat.analyzer.dupont_analyzer import DupontAnalyzer

import datetime
import unittest

class CapitalIncreaseHistoryAnalyzerTest(unittest.TestCase):
    def test_get_analysis_2330(self):
        analyzer = DupontAnalyzer('2330')
        roe = analyzer.get_roe().get()
        print roe
