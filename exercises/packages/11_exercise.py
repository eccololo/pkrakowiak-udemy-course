# Wykorzystując moduł wbudowany datetime oraz klasy
# date oraz timedelta z podanej daty 2020-01-01 00:00:00 otrzymaj datę:
#
# przesuniętą o 7 dni
#
# przesuniętą o 30 dni
#
# przesuniętą o 30 godzin
#
# przesuniętą o 15 minut

import datetime

print(help(datetime.timedelta))

dt1 = datetime.datetime(2020, 1, 1, 0, 0, 0)

tdelta1 = dt1 + datetime.timedelta(days=7)
tdelta2 = dt1 + datetime.timedelta(days=30)
tdelta3 = dt1 + datetime.timedelta(hours=30)
tdelta4 = dt1 + datetime.timedelta(minutes=15)

print(tdelta1)
print(tdelta2)
print(tdelta3)
print(tdelta4)