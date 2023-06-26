# 2020-07-21 a 2020-12-31.

import datetime

d1 = datetime.date(2020, 7, 21)
d2 = datetime.date(2020, 12, 31)

delta = d2 - d1

print(f"Number of days: {delta.days}")