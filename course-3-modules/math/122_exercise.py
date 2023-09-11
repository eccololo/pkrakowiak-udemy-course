import math
import random
from random import random as rand


random.seed(42)
centroid = (0.5, 0.5)
points = [(rand(), rand()) for i in range(10)]

closest = 100
output = None
for idx, point in enumerate(points):
    distance = math.dist(centroid, point)
    if distance < closest:
        closest = distance
        output = (idx, closest)

print(output)