import math


def calculate_seq(n):
    return (1 + 1 / n) ** n


output = [calculate_seq(i) for i in range(1, 21)]
for item in output:
    print(item)
