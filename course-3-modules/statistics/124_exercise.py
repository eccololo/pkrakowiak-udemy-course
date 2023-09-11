import statistics
import random


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

random.seed(42)
mean = statistics.mean(data)
odchylenie_standardowe = statistics.stdev(data)

result = statistics.NormalDist(mean, odchylenie_standardowe).samples(10)
result = [round(item, 3) for item in result]
print(result)
