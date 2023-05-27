# Wykorzystując moduł wbudowany datetime wyznacz wartość przyszłą
# (future value) kapitału początkowego (present value) 1000 USD
# przy rocznej stopie procentowej 4% (rate) i kapitalizacji złożonej
# dziennej odsetek zakładając czas trwania inwestycji od 2021-07-01
# do 2021-12-31. Do obliczeń przyjmij, że rok ma 365 dni.

import datetime

dt1 = datetime.date(2021, 7, 1)
dt2 = datetime.date(2021, 12, 31)

delta_d = (dt2 - dt1).days

rate = 0.04
pv = 1000
daily_rate = rate / 365.0
total = round(pv * pow((1 + daily_rate), delta_d), 2)

print(f"Future value: {total} USD")