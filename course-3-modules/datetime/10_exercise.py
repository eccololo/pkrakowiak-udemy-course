from datetime import datetime

date_now = datetime.now()
year_now = datetime.now().year + 1
date_end_year = datetime(year_now, 1, 1)

delta = abs(date_end_year - date_now)

output = f'Until the end of the year: {delta}'

print(output)