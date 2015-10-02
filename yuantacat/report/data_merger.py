#-*- coding: utf-8 -*-

class DataMerger():
    def merge(self, param):
        data = param['data'] 
        category_field = param['category_field']
        output = []
        stmt_dates = self.__merge_stmt_dates(data)
        for stmt_date in stmt_dates: 
            merged = { 'date' : self.__format_date(stmt_date, category_field) }
            for account in data:
                value_format = data[account]['format']
                for account_stmt_date, account_value in data[account]['value']:
                    if stmt_date == account_stmt_date:
                        merged[account] = self.__format_value(account_value, value_format)
            output.append(merged)
        return output

    def __format_date(self, date, category_field):
        if category_field == 'year':
            return str(date.year)    
        else:
            return str(date)

    def __format_value(self, value, format):
        if format == 'percentage':
            return value * 100
        elif format == 'integer':
            return int(value)
        else:
            return value

    def __merge_stmt_dates(self, data):
        all_stmt_dates = set()
        for account in data:
            for stmt_date, value in data[account]['value']:
                all_stmt_dates.add(stmt_date)
        return sorted(list(all_stmt_dates))
