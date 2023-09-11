import math

r = 0.04
pv = 1000
fv = 2000
e = math.e
years = (1 / r) * math.log(fv / pv)

print(f"n = {math.ceil(years)}")
