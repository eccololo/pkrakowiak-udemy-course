from datetime import date

rate = 0.04
pv = 1000
daily_rate = rate / 365.0

date_start = date(2021, 7, 1)
date_end = date(2021, 12, 31)

delta = abs(date_end - date_start).days
output = pv * (1 + daily_rate)**delta

print(f"Future value: {round(output, 2)} USD")