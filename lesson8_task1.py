class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i != '-': my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2020 >= year >= 0:
                    return f'Everything OK!'
                else:
                    return f'Wrong year'
            else:
                return f'Wrong month'
        else:
            return f'Wrong day'

    def __str__(self):
        return f'Current date {Data.extract(self.day_month_year)}'


today = Data('27 - 5 - 2020')
print(today)
print(Data.valid(20, 10, 2030))
print(today.valid(18, 15, 2015))
print(Data.extract('25 - 12 - 2017'))
print(today.extract('12 - 10 - 2019'))
print(Data.valid(29, 10, 2009))
