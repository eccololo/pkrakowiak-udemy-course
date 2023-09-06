import random


techs = ['python', 'java', 'php', 'c++', 'c#', 'javascript']
random.seed(32)
# print(random.choices(techs, weights=[1, 1, 1, 1, 1, 1], k=3))

# other solution
print(random.choices(population=techs, k=3))