import math

chance = 1 / math.comb(49, 6)
print(f"{100 * chance:.10f}%")