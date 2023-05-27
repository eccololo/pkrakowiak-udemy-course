import datetime

dt1 = datetime.datetime.now()
dt2 = datetime.datetime(2024, 1, 1)

delta = dt2 - dt1

print(f"Until the end of the year: {delta}")