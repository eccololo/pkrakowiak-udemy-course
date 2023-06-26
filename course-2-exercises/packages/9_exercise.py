'Number of days until the end of the year: x'

import datetime

dt_now = datetime.date.today()
dt_year_end = datetime.date(2023, 12, 31)

delta = (dt_year_end - dt_now).days

print(f"Number of days until the end of the year: {delta}")