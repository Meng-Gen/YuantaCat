#-*- coding: utf-8 -*-

from yuantacat.pipeline.pipeline import Pipeline
from yuantacat.spider.income_statement_spider import IncomeStatementQuarterlySpider
from yuantacat.spider.income_statement_spider import IncomeStatementYearlySpider
from yuantacat.assembler.income_statement_assembler import IncomeStatementQuarterlyAssembler
from yuantacat.assembler.income_statement_assembler import IncomeStatementYearlyAssembler
from yuantacat.feed.income_statement_feed import IncomeStatementFeedBuilder

class IncomeStatementQuarterlyPipeline(Pipeline):
    def __init__(self):
        param = {
            'memento_path' : './yuantacat/data/memento/income_statement_quarterly.json',
            'default_value_param' : 'stock_symbol',
            'spider' : IncomeStatementQuarterlySpider(), 
            'assembler' : IncomeStatementQuarterlyAssembler(), 
            'feed_builder' : IncomeStatementFeedBuilder(),
        }
        Pipeline.__init__(self, param)

class IncomeStatementYearlyPipeline(Pipeline):
    def __init__(self):
        param = {
            'memento_path' : './yuantacat/data/memento/income_statement_yearly.json',
            'default_value_param' : 'stock_symbol',
            'spider' : IncomeStatementYearlySpider(), 
            'assembler' : IncomeStatementYearlyAssembler(), 
            'feed_builder' : IncomeStatementFeedBuilder(),
        }
        Pipeline.__init__(self, param)