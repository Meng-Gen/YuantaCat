#-*- coding: utf-8 -*-

class AnalyzerUtils():
    def get_time_series(self, records):
        group = {}
        for record in records:
            release_date, stmt_date, value = record
            if stmt_date not in group:
                group[stmt_date] = []
            group[stmt_date].append((release_date, value))

        time_series = []
        for stmt_date in group:
            latest_date, value = sorted(group[stmt_date])[-1]
            time_series.append((stmt_date, value))

        return sorted(time_series)
