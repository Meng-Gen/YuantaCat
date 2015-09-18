#-*- coding: utf-8 -*-

from yuantacat.feed.feed import Feed
from yuantacat.feed.yuanta_feed_builder import YuantaFeedBuilder

class DividendPolicyFeed(Feed):
    pass

class DividendPolicyFeedBuilder():
    def build(self, dao):
        builder = YuantaFeedBuilder([u'現金股利', u'盈餘配股', u'公積配股', u'員工配股率'], [1, 2, 3, 6])
        tuple_feed = builder.build(dao)
        return DividendPolicyFeed(tuple_feed)
