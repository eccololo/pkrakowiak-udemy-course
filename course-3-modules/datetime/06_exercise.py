import datetime

first_date = datetime.datetime(2020, 7, 20, 11, 30, 0)
second_date = datetime.datetime(2021, 2, 20, 10, 25, 0)

delta = abs(first_date - second_date)

print(delta)