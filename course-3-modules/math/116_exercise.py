import math


def calculate_seq(n):
    return (1 + (1 / n)) ** n


counter = 1
while not math.isclose(calculate_seq(counter), math.e, rel_tol=1e-06):
    counter += 1

print(counter)
