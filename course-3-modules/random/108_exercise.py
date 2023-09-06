import random

random.seed(42)

numbers = [round(random.uniform(5, 10), 4) for i in range(10)]

print(numbers)