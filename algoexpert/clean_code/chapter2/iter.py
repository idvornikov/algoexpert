from datetime import date, timedelta


class DateRangeIterable:
    def __init__(self, start_date: date, end_date: date):
        self.start_date = start_date
        self.end_date = end_date
        self._present_day = start_date

    def __iter__(self):
        current_day = self._present_day
        while current_day < self.end_date:
            yield current_day
            current_day += timedelta(days=1)

    # def __next__(self):
    #     if self._present_day >= self.end_date:
    #         raise StopIteration
    #     current_date = self._present_day
    #     self._present_day += timedelta(days=1)
    #     return current_date


if __name__ == '__main__':
    for day in DateRangeIterable(date(2020, 11, 10), date(2020, 11, 20)):
        print(day)
