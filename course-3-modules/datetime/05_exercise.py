import datetime

first_date = datetime.date(2020, 7, 21)
second_date = datetime.date(2020, 12, 31)

delta = abs(first_date - second_date).days

print(f"Number of days: {delta}")