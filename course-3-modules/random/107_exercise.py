import random

random.seed(42)

numbers = []

for i in range(10):
    numbers.append(round(random.random(), 4))

print(numbers)