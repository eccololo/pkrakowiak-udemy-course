def even_numbers(n):
    # Enter your solution here
    for i in range(n):
        if i % 2 == 0:
            yield i


for number in even_numbers(10):
    print(number, end=',')

print()

for number in even_numbers(30):
    print(number, end=',')
