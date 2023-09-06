import random


random.seed(32)
techs = ['python', 'java', 'php', 'c++', 'c#', 'javascript']

print(random.sample(techs, k=3))