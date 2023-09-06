import random

random.seed(42)

numbers = [random.randint(1, 49) for _ in range(6)]

print(numbers)