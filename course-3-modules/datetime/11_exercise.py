from datetime import datetime, timedelta

date_1 = datetime(2020,1,1)

new_date_1 = date_1 + timedelta(days=7)
new_date_2 = date_1 + timedelta(days=30)
new_date_3 = date_1 + timedelta(hours=30)
new_date_4 = date_1 + timedelta(minutes=15)

print(new_date_1)
print(new_date_2)
print(new_date_3)
print(new_date_4)