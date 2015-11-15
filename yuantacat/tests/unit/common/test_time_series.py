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

    def test_accumulate_annually(self):
        x = TimeSeries([
            (datetime.date(2001, 3, 31), 1),
            (datetime.date(2001, 6, 30), 2),
            (datetime.date(2001, 9, 30), 3),
            (datetime.date(2001, 12, 31), 4),
        ])
        z = x.accumulate_annually()
        self.assertEqual(z.get(), [
            (datetime.date(2001, 3, 31), 1), 
            (datetime.date(2001, 6, 30), 3),
            (datetime.date(2001, 9, 30), 6),
            (datetime.date(2001, 12, 31), 10),
        ])        

    def test_shift(self):
        x = TimeSeries([
            (datetime.date(2001, 3, 31), 1),
            (datetime.date(2001, 6, 30), 2),
            (datetime.date(2001, 9, 30), 3),
            (datetime.date(2001, 12, 31), 4),
        ])
        z = x.shift()
        self.assertEqual(z.get(), [
            (datetime.date(2001, 6, 30), 1),
            (datetime.date(2001, 9, 30), 2),
            (datetime.date(2001, 12, 31), 3),
        ])

    def test_group_by_period_Q(self):
        x = TimeSeries([
            (datetime.date(2001, 1, 31), 1),
            (datetime.date(2001, 2, 28), 2),
            (datetime.date(2001, 3, 31), 3),
            (datetime.date(2001, 4, 30), 4),
            (datetime.date(2001, 5, 31), 5),
            (datetime.date(2001, 6, 30), 6),
            (datetime.date(2001, 7, 31), 7),
            (datetime.date(2001, 8, 31), 8),
            (datetime.date(2001, 9, 30), 9),
            (datetime.date(2001, 10, 31), 10),
            (datetime.date(2001, 11, 30), 11),
            (datetime.date(2001, 12, 31), 12),
        ])
        z = x.group_by_period('Q')
        z_map = z.get_map()
        self.assertEqual(z_map[datetime.date(2001, 3, 31)].get(), [
            (datetime.date(2001, 1, 31), 1),
            (datetime.date(2001, 2, 28), 2),
            (datetime.date(2001, 3, 31), 3),
        ])
        self.assertEqual(z_map[datetime.date(2001, 6, 30)].get(), [
            (datetime.date(2001, 4, 30), 4),
            (datetime.date(2001, 5, 31), 5),
            (datetime.date(2001, 6, 30), 6),
        ])
        self.assertEqual(z_map[datetime.date(2001, 9, 30)].get(), [
            (datetime.date(2001, 7, 31), 7),
            (datetime.date(2001, 8, 31), 8),
            (datetime.date(2001, 9, 30), 9),
        ])
        self.assertEqual(z_map[datetime.date(2001, 12, 31)].get(), [
            (datetime.date(2001, 10, 31), 10),
            (datetime.date(2001, 11, 30), 11),
            (datetime.date(2001, 12, 31), 12),
        ])

    def test_group_by_period_Y(self):
        x = TimeSeries([
            (datetime.date(2001, 1, 31), 1),
            (datetime.date(2001, 2, 28), 2),
            (datetime.date(2001, 3, 31), 3),
            (datetime.date(2001, 4, 30), 4),
            (datetime.date(2001, 5, 31), 5),
            (datetime.date(2001, 6, 30), 6),
            (datetime.date(2001, 7, 31), 7),
            (datetime.date(2001, 8, 31), 8),
            (datetime.date(2001, 9, 30), 9),
            (datetime.date(2001, 10, 31), 10),
            (datetime.date(2001, 11, 30), 11),
            (datetime.date(2001, 12, 31), 12),
        ])
        z = x.group_by_period('Y')
        z_map = z.get_map()
        self.assertEqual(z_map[datetime.date(2001, 12, 31)].get(), [
            (datetime.date(2001, 1, 31), 1),
            (datetime.date(2001, 2, 28), 2),
            (datetime.date(2001, 3, 31), 3),
            (datetime.date(2001, 4, 30), 4),
            (datetime.date(2001, 5, 31), 5),
            (datetime.date(2001, 6, 30), 6),
            (datetime.date(2001, 7, 31), 7),
            (datetime.date(2001, 8, 31), 8),
            (datetime.date(2001, 9, 30), 9),
            (datetime.date(2001, 10, 31), 10),
            (datetime.date(2001, 11, 30), 11),
            (datetime.date(2001, 12, 31), 12),
        ])

    def test_get_max_by_period_Q(self):
        x = TimeSeries([
            (datetime.date(2001, 1, 31), 1),
            (datetime.date(2001, 2, 28), 2),
            (datetime.date(2001, 3, 31), 3),
            (datetime.date(2001, 4, 30), 4),
            (datetime.date(2001, 5, 31), 5),
            (datetime.date(2001, 6, 30), 6),
            (datetime.date(2001, 7, 31), 7),
            (datetime.date(2001, 8, 31), 8),
            (datetime.date(2001, 9, 30), 9),
            (datetime.date(2001, 10, 31), 10),
            (datetime.date(2001, 11, 30), 11),
            (datetime.date(2001, 12, 31), 12),
        ])
        z = x.get_max_by_period('Q')
        self.assertEqual(z.get(), [
            (datetime.date(2001, 3, 31), 3),
            (datetime.date(2001, 6, 30), 6),
            (datetime.date(2001, 9, 30), 9),
            (datetime.date(2001, 12, 31), 12),
        ])

    def test_get_max_by_period_Y(self):
        x = TimeSeries([
            (datetime.date(2001, 1, 31), 1),
            (datetime.date(2001, 2, 28), 2),
            (datetime.date(2001, 3, 31), 3),
            (datetime.date(2001, 4, 30), 4),
            (datetime.date(2001, 5, 31), 5),
            (datetime.date(2001, 6, 30), 6),
            (datetime.date(2001, 7, 31), 7),
            (datetime.date(2001, 8, 31), 8),
            (datetime.date(2001, 9, 30), 9),
            (datetime.date(2001, 10, 31), 10),
            (datetime.date(2001, 11, 30), 11),
            (datetime.date(2001, 12, 31), 12),
        ])
        z = x.get_max_by_period('Y')
        self.assertEqual(z.get(), [
            (datetime.date(2001, 12, 31), 12),
        ])

    def test_get_min_by_period_Q(self):
        x = TimeSeries([
            (datetime.date(2001, 1, 31), 1),
            (datetime.date(2001, 2, 28), 2),
            (datetime.date(2001, 3, 31), 3),
            (datetime.date(2001, 4, 30), 4),
            (datetime.date(2001, 5, 31), 5),
            (datetime.date(2001, 6, 30), 6),
            (datetime.date(2001, 7, 31), 7),
            (datetime.date(2001, 8, 31), 8),
            (datetime.date(2001, 9, 30), 9),
            (datetime.date(2001, 10, 31), 10),
            (datetime.date(2001, 11, 30), 11),
            (datetime.date(2001, 12, 31), 12),
        ])
        z = x.get_min_by_period('Q')
        self.assertEqual(z.get(), [
            (datetime.date(2001, 3, 31), 1),
            (datetime.date(2001, 6, 30), 4),
            (datetime.date(2001, 9, 30), 7),
            (datetime.date(2001, 12, 31), 10),
        ])

    def test_get_min_by_period_Y(self):
        x = TimeSeries([
            (datetime.date(2001, 1, 31), 1),
            (datetime.date(2001, 2, 28), 2),
            (datetime.date(2001, 3, 31), 3),
            (datetime.date(2001, 4, 30), 4),
            (datetime.date(2001, 5, 31), 5),
            (datetime.date(2001, 6, 30), 6),
            (datetime.date(2001, 7, 31), 7),
            (datetime.date(2001, 8, 31), 8),
            (datetime.date(2001, 9, 30), 9),
            (datetime.date(2001, 10, 31), 10),
            (datetime.date(2001, 11, 30), 11),
            (datetime.date(2001, 12, 31), 12),
        ])
        z = x.get_min_by_period('Y')
        self.assertEqual(z.get(), [
            (datetime.date(2001, 12, 31), 1),
        ])