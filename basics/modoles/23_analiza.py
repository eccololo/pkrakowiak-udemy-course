import rocket_science

print(dir(rocket_science))
print(rocket_science.calculate_mean([3, 4, 5, 6]))
print(rocket_science.calculate_min([3, 4, 5, 6]))
print(rocket_science.calculate_max([3, 4, 5, 6]))

from rocket_science import calculate_min, calculate_max

print(calculate_min([99, 101, 1]))
print(calculate_max([10, 101, 1001]))
