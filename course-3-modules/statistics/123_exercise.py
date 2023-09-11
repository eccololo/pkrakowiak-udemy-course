import statistics as s


data = [
    59.19,
    72.05,
    66.82,
    81.15,
    66.33,
    94.87,
    99.65,
    70.13,
    55.75,
    87.71,
    95.43,
    93.17,
    98.54,
    68.31,
    59.24,
    88.94,
    79.44,
    83.91,
    84.4,
    68.21,
]

srednia_arytmetyczna = s.mean(data)
srednia_geometryczna = s.geometric_mean(data)
srednia_harmoniczna = s.harmonic_mean(data)
mediana = s.median(data)

print(f"{round(srednia_arytmetyczna, 2)}")
print(f"{round(srednia_geometryczna, 2)}")
print(f"{round(srednia_harmoniczna, 2)}")
print(f"{round(mediana, 2)}")
