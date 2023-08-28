def geometric_sequence(a, q, n):
    # Enter your solution here
    for i in range(n):
        yield a * q ** i


for num in geometric_sequence(1, 2, 10):
    print(num, end=',')

print()

for num in geometric_sequence(1, 4, 10):
    print(num, end=',')

print()

for num in geometric_sequence(1, 0.5, 5):
    print(num, end=',')