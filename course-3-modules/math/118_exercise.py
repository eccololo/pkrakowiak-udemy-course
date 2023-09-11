import math

for k in range(6, -1, -1):
    hits = math.comb(6, k) * math.comb(49 - 6, 6 - k)
    result = hits / math.comb(49, 6)
    print(f"hit: {k} prob: {100 * result:.10f}%")