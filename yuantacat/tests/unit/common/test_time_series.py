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
        self.assertEqual(len(time_series), 2)
        self.assertEqual(time_series[0], (datetime.date(2001, 12, 31), 2))
        self.assertEqual(time_series[1], (datetime.date(2002, 12, 31), 1))

    def test_average(self):
        time_series = TimeSeries([
            (datetime.date(2001, 12, 31), 1),
            (datetime.date(2002, 12, 31), 2),
            (datetime.date(2003, 12, 31), 3),
            (datetime.date(2004, 12, 31), 4),
            (datetime.date(2005, 12, 31), 6),
        ])
        averaged = time_series.average().get()
        self.assertEqual(len(averaged), 5)
        self.assertEqual(averaged[0], (datetime.date(2001, 12, 31), 1))
        self.assertEqual(averaged[1], (datetime.date(2002, 12, 31), 1.5))
        self.assertEqual(averaged[2], (datetime.date(2003, 12, 31), 2.5))
        self.assertEqual(averaged[3], (datetime.date(2004, 12, 31), 3.5))
        self.assertEqual(averaged[4], (datetime.date(2005, 12, 31), 5))
