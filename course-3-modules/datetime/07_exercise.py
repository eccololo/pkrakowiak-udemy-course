from datetime import datetime

date_x = datetime(2021, 4, 20, 11, 30, 0)

print(date_x.strftime("%Y-%m-%d"))
print(date_x.strftime("%d-%m-%Y"))
print(date_x.strftime("%m-%Y"))
print(date_x.strftime("%B-%Y"))
print(date_x.strftime("%d %B, %Y"))
print(date_x.strftime("%Y-%m-%d %I:%M:%S"))
print(date_x.strftime("%m/%d/%Y %I:%M:%S"))
print(date_x.strftime("%d(%a) %B %Y"))