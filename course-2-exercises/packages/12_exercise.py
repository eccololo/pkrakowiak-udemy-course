import datetime

dt1 = datetime.datetime(2020, 1, 1, 0, 0)
tdelta1 = datetime.timedelta(hours=8)
dates = []
dates.append(dt1)

for _ in range(11):
    dt1 += tdelta1
    dates.append(dt1)

for date in dates:
    print(date)