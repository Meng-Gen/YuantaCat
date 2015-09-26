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

    def test_get_scalar(self):
        x = TimeSeries([
            (datetime.date(2001, 12, 31), 1),
            (datetime.date(2002, 12, 31), 2),
            (datetime.date(2003, 12, 31), 5),
        ])
        y = x.scalar(2)
        self.assertEqual(y.get(), [
            (datetime.date(2001, 12, 31), 2.0), 
            (datetime.date(2002, 12, 31), 4.0),
            (datetime.date(2003, 12, 31), 10.0),
        ])

    def test_get_inverse(self):
        x = TimeSeries([
            (datetime.date(2001, 12, 31), 1),
            (datetime.date(2002, 12, 31), 2),
            (datetime.date(2003, 12, 31), 5),
        ])
        y = x.get_inverse()
        self.assertEqual(y.get(), [
            (datetime.date(2001, 12, 31), 1.0), 
            (datetime.date(2002, 12, 31), 0.5),
            (datetime.date(2003, 12, 31), 0.2),
        ])

    def test_get_average(self):
        time_series = TimeSeries([
            (datetime.date(2001, 12, 31), 1),
            (datetime.date(2002, 12, 31), 2),
            (datetime.date(2003, 12, 31), 3),
            (datetime.date(2004, 12, 31), 4),
            (datetime.date(2005, 12, 31), 6),
        ])
        averaged = time_series.get_average()
        self.assertEqual(averaged.get(), [
            (datetime.date(2001, 12, 31), 1),
            (datetime.date(2002, 12, 31), 1.5),
            (datetime.date(2003, 12, 31), 2.5),
            (datetime.date(2004, 12, 31), 3.5),
            (datetime.date(2005, 12, 31), 5),
        ])

    def test_add(self):
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
        z = x + y
        self.assertEqual(z.get(), [
            (datetime.date(2001, 12, 31), 6.0), 
            (datetime.date(2002, 12, 31), 4.0),
            (datetime.date(2003, 12, 31), 4.0),
        ])

    def test_minus(self):
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
        z = x - y
        self.assertEqual(z.get(), [
            (datetime.date(2001, 12, 31), -4.0), 
            (datetime.date(2002, 12, 31), 0.0),
            (datetime.date(2003, 12, 31), 2.0),
        ])

    def test_divide(self):
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
        z = x / y
        self.assertEqual(z.get(), [
            (datetime.date(2001, 12, 31), 0.2), 
            (datetime.date(2002, 12, 31), 1.0),
            (datetime.date(2003, 12, 31), 3.0),
        ])

    def test_multiply(self):
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
        z = x * y
        self.assertEqual(z.get(), [
            (datetime.date(2001, 12, 31), 5.0), 
            (datetime.date(2002, 12, 31), 4.0),
            (datetime.date(2003, 12, 31), 3.0),
        ]) 

    def test_accumulate(self):
        x = TimeSeries([
            (datetime.date(2001, 3, 31), 1),
            (datetime.date(2001, 6, 30), 2),
            (datetime.date(2001, 9, 30), 3),
            (datetime.date(2001, 12, 31), 4),
        ])
        z = x.accumulate()
        self.assertEqual(z.get(), [
            (datetime.date(2001, 3, 31), 1), 
            (datetime.date(2001, 6, 30), 3),
            (datetime.date(2001, 9, 30), 6),
            (datetime.date(2001, 12, 31), 10),
        ])        
