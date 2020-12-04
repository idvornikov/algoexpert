from datetime import timedelta, date


class DateRangeSequence:
    def __init__(self, start_date, end_date):
        self._start_date = start_date
        self._end_date = end_date
        self._range = self._create_range()

    def _create_range(self):
        current_day = self._start_date
        days = []
        while current_day < self._end_date:
            days.append(current_day)
            current_day += timedelta(days=1)
        return days

    def __getitem__(self, item):
        return self._range[item]

    def __len__(self):
        return len(self._range)


if __name__ == '__main__':
    date_sequence = DateRangeSequence(date(2020, 11, 21), date(2020, 11, 28))
    # for day in date_sequence:
    #     print(day)
    print(date_sequence[3])
