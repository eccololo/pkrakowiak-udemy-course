limit = 100
number = 1
next_number = 1
output = number
print(0)
print(1)
while output < limit:
    print(output)
    output = number + next_number
    number = next_number
    next_number = output

# Other solution
a, b = 0, 1
limit = 100

while a < limit:
    print(a)
    a, b = b, a + b
