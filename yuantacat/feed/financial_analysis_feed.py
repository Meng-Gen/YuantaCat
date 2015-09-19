#-*- coding: utf-8 -*-

from yuantacat.feed.feed import Feed
from yuantacat.feed.financial_feed_builder import FinancialFeedBuilder

class FinancialAnalysisFeed(Feed):
    pass 

class FinancialAnalysisFeedBuilder():
    def build(self, dao):
        tuple_feed = FinancialFeedBuilder().build(dao)
        return FinancialAnalysisFeed(tuple_feed)
