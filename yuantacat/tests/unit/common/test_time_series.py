#-*- coding: utf-8 -*-

from yuantacat.common.time_series import TimeSeries

import datetime
import unittest

class TimeSeriesTest(unittest.TestCase):
    def test_create_time_series(self):
        records = [
            (datetime.date(2015, 9, 30), datetime.date(2002, 12, 31), 1), 
            (datetime.date(2015, 9, 30), datetime.date(2001, 12, 31), 2), 
            (datetime.date(2015, 8, 31), datetime.date(2001, 12, 31), 3), 
        ]
        time_series = TimeSeries.create(records).get()
        self.assertEqual(time_series, [
            (datetime.date(2001, 12, 31), 2),
            (datetime.date(2002, 12, 31), 1),
        ])

    def test_get_map(self):
        time_series = TimeSeries([
            (datetime.date(2001, 12, 31), 1),
            (datetime.date(2002, 12, 31), 2),
            (datetime.date(2003, 12, 31), 3),
        ])
        time_series_map = time_series.get_map()
        self.assertEqual(time_series_map, {
            datetime.date(2001, 12, 31) : 1,
            datetime.date(2002, 12, 31) : 2,
            datetime.date(2003, 12, 31) : 3,
        })

    def test_get_average(self):
        time_series = TimeSeries([
            (datetime.date(2001, 12, 31), 1),
            (datetime.date(2002, 12, 31), 2),
            (datetime.date(2003, 12, 31), 3),
            (datetime.date(2004, 12, 31), 4),
            (datetime.date(2005, 12, 31), 6),
        ])
        averaged = time_series.get_average().get()
        self.assertEqual(averaged, [
            (datetime.date(2001, 12, 31), 1),
            (datetime.date(2002, 12, 31), 1.5),
            (datetime.date(2003, 12, 31), 2.5),
            (datetime.date(2004, 12, 31), 3.5),
            (datetime.date(2005, 12, 31), 5),
        ])

    def test_get_ratio(self):
        x = TimeSeries([
            (datetime.date(2001, 12, 31), 1),
            (datetime.date(2002, 12, 31), 2),
            (datetime.date(2003, 12, 31), 3),
        ])
        y = TimeSeries([
            (datetime.date(2001, 12, 31), 5),
            (datetime.date(2002, 12, 31), 2),
            (datetime.date(2003, 12, 31), 1),
        ])
        ratio = x.get_ratio(y).get()
        self.assertEqual(ratio, [
            (datetime.date(2001, 12, 31), 0.2), 
            (datetime.date(2002, 12, 31), 1.0),
            (datetime.date(2003, 12, 31), 3.0),
        ])
