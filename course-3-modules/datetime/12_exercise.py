from datetime import datetime, timedelta

date_start = datetime(2020,1,1,0,0,0)
end_date = datetime(2020, 1, 4, 16, 0, 0)
dates = [date_start]

while date_start != end_date:
    date_start = date_start + timedelta(hours=8)
    dates.append(date_start)

for date in dates:
    print(date)