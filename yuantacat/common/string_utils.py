#-*- coding: utf-8 -*-

from yuantacat.common.date_utils import DateUtils

import calendar
import datetime
import re

class StringBuilder():
    def build(self, local_string):
        decoded_string = self.__decode(local_string)
        return decoded_string.replace('&nbsp;', ' ')

    # chain of responsibility: try any possible codec
    def __decode(self, local_string):
        try:
            return local_string.decode('utf-8')
        except UnicodeDecodeError:
            return self.__decode_step_1(local_string)

    def __decode_step_1(self, local_string):
        try:
            return local_string.decode('big5-hkscs', 'ignore')
        except UnicodeDecodeError:
            return self.__decode_step_2(local_string)

    def __decode_step_2(self, local_string):
        return local_string.decode('gb18030')

class NumberBuilder():
    def build(self, number_string):
        # remove comma style
        number_string = number_string.replace(',', '')
        # try to parse negative sign from parentheses 
        try:
            m = re.search('^\((.+)\)$', number_string)
            return -int(m.group(1))
        except AttributeError:
            return self.__build_step_1(number_string)

    def __build_step_1(self, number_string):
        try:
            return int(number_string)
        except ValueError:
            return self.__build_step_2(number_string)

    def __build_step_2(self, number_string):
        try:
            return float(number_string)
        except ValueError:
            return self.__build_step_3(number_string)

    def __build_step_3(self, number_string):
        try:
            m = re.search('^(.+)%$', number_string)
            return float(m.group(1)) * 0.01
        except AttributeError:
            return self.__build_step_4(number_string)

    def __build_step_4(self, number_string):
        if number_string.strip() in [u'-', u'', u'不適用', u'N/A']:
            return None
        else: 
            raise ValueError

class DateBuilder(): 
    def __init__(self):
        self.date_utils = DateUtils()

    def build(self, local_string):
        try:
            m = re.search(u'^(\d{4})年(\d+)月(\d+)日$', local_string)
            year = int(m.group(1))
            month = int(m.group(2))
            day = int(m.group(3))
            return datetime.date(year, month, day)
        except AttributeError:
            return self.__build_step_1(local_string)

    def __build_step_1(self, local_string):
        try:
            m = re.search(u'^(\d{2,3})年(\d+)月(\d+)日$', local_string)
            year = int(m.group(1)) + 1911 # expect roc era
            month = int(m.group(2))
            day = int(m.group(3))
            return datetime.date(year, month, day)
        except AttributeError:
            return self.__build_step_2(local_string)

    def __build_step_2(self, local_string):    
        try:
            m = re.search('^(\d{4})/(\d+)/(\d+)$', local_string)
            year = int(m.group(1))
            month = int(m.group(2))
            day = int(m.group(3))
            return datetime.date(year, month, day)
        except AttributeError:
            return self.__build_step_3(local_string)

    def __build_step_3(self, local_string):    
        try:
            m = re.search('^(\d{2,3})/(\d+)/(\d+)$', local_string)
            year = int(m.group(1)) + 1911 # expect roc era
            month = int(m.group(2))
            day = int(m.group(3))
            return datetime.date(year, month, day)
        except AttributeError:
            return self.__build_step_4(local_string)

    def __build_step_4(self, local_string):    
        try:
            m = re.search('^(\d{2,3})$', local_string)
            year = int(m.group(1)) + 1911 # expect roc era
            return datetime.date(year, 12, 31)
        except AttributeError:
            return self.__build_step_5(local_string)

    def __build_step_5(self, local_string):    
        try:
            m = re.search('^(\d{2,3})\.(\d{1})Q$', local_string)
            year = int(m.group(1)) + 1911 # expect roc era
            end_quarter = int(m.group(2))
            return self.__from_year_quarter_to_date(year, end_quarter)
        except AttributeError:
            return self.__build_step_6(local_string)

    def __build_step_6(self, local_string):    
        try:
            m = re.search('^(\d{2,3})/0?(\d{1,2})$', local_string)
            year = int(m.group(1)) + 1911 # expect roc era
            month = int(m.group(2))
            day = self.date_utils.get_last_day_of_month(year, month)
            return datetime.date(year, month, day)
        except AttributeError:
            return self.__build_step_7(local_string)

    def __build_step_7(self, local_string):
        m = re.search(u'^民國(\d{2,3})年(\d+)月$', local_string)
        year = int(m.group(1)) + 1911 # expect roc era
        month = int(m.group(2))
        day = self.date_utils.get_last_day_of_month(year, month)
        return datetime.date(year, month, day)

    def __from_year_quarter_to_date(self, year, quarter):
        if quarter == 1:
            return datetime.date(year, 3, 31)
        if quarter == 2:
            return datetime.date(year, 6, 30)
        if quarter == 3:
            return datetime.date(year, 9, 30)
        if quarter == 4:
            return datetime.date(year, 12, 31)

class StringUtils():
    def __init__(self):
        self.date_builder = DateBuilder()
        self.number_builder = NumberBuilder()
        self.string_builder = StringBuilder()

    def normalize_number(self, number_string):
        return self.number_builder.build(number_string)

    def normalize_string(self, local_string):
        return self.string_builder.build(local_string)

    def from_local_string_to_date(self, local_string):
        return self.date_builder.build(local_string)

    def from_date_to_roc_era_string(self, date):
        return str(date.year - 1911)

    def from_date_to_2_digit_month_string(self, date):
        return '{0:02d}'.format(date.month) 

    def from_date_to_2_digit_quarter_string(self, date):
        quarter = (date.month - 1) // 3 + 1
        return '{0:02d}'.format(quarter) 

    def from_date_to_1_digit_quarter_string(self, date):
        quarter = (date.month - 1) // 3 + 1
        return str(quarter)
        
    def is_match(self, regex, string):
        return re.match(regex, string) is not None

    def match(self, regex, string):
        m = re.search(regex, string)
        return list(m.groups()) if m else []