#-*- coding: utf-8 -*-

from yuantacat.pipeline.pipeline import Pipeline
from yuantacat.spider.financial_analysis_spider import FinancialAnalysisQuarterlySpider
from yuantacat.spider.financial_analysis_spider import FinancialAnalysisYearlySpider
from yuantacat.assembler.financial_analysis_assembler import FinancialAnalysisQuarterlyAssembler
from yuantacat.assembler.financial_analysis_assembler import FinancialAnalysisYearlyAssembler
from yuantacat.feed.financial_analysis_feed import FinancialAnalysisFeedBuilder

class FinancialAnalysisQuarterlyPipeline(Pipeline):
    def __init__(self):
        param = {
            'memento_path' : './yuantacat/data/memento/financial_analysis_quarterly.json',
            'default_value_param' : 'stock_symbol',
            'spider' : FinancialAnalysisQuarterlySpider(), 
            'assembler' : FinancialAnalysisQuarterlyAssembler(), 
            'feed_builder' : FinancialAnalysisFeedBuilder(),
        }
        Pipeline.__init__(self, param)

class FinancialAnalysisYearlyPipeline(Pipeline):
    def __init__(self):
        param = {
            'memento_path' : './yuantacat/data/memento/financial_analysis_yearly.json',
            'default_value_param' : 'stock_symbol',
            'spider' : FinancialAnalysisYearlySpider(), 
            'assembler' : FinancialAnalysisYearlyAssembler(), 
            'feed_builder' : FinancialAnalysisFeedBuilder(),
        }
        Pipeline.__init__(self, param)