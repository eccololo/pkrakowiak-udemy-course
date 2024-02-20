from datetime import datetime

date_now = datetime.now()
year_now = datetime.now().year
date_end_year = datetime(year_now, 12, 31)

delta = abs(date_end_year - date_now).days + 1 # + present day

output = f'Number of days until the end of the year: {delta}'

print(output)