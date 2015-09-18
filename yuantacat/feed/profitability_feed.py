#-*- coding: utf-8 -*-

from yuantacat.feed.feed import Feed
from yuantacat.feed.yuanta_feed_builder import YuantaFeedBuilder

class ProfitabilityFeed(Feed):
    pass

class ProfitabilityFeedBuilder():
    def build(self, dao):
        builder = YuantaFeedBuilder([u'營業收入', u'營業成本', u'營業毛利', u'毛利率', u'營業利益', u'營益率', u'業外收支', u'稅前淨利', u'稅後淨利'], [1, 2, 3, 4, 5, 6, 7, 8, 9])
        tuple_feed = builder.build(dao)
        return ProfitabilityFeed(tuple_feed)
