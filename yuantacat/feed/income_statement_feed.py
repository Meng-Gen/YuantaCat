#-*- coding: utf-8 -*-

from yuantacat.feed.feed import Feed
from yuantacat.feed.financial_feed_builder import FinancialFeedBuilder

class IncomeStatementFeed(Feed):
    pass 

class IncomeStatementFeedBuilder():
    def build(self, dao):
        tuple_feed = FinancialFeedBuilder().build(dao)
        return IncomeStatementFeed(tuple_feed)
