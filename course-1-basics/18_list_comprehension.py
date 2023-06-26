# Tradycyjna metoda
result = []
for i in range(100):
    result.append(i ** 2)

# List Comprehension
# [co ma robić - pętla]
result = [i ** 2 for i in range(100)]

print(result)

# Tradycyjna metoda
result = []
for i in range(100):
    if i % 5 == 0:
        result.append(i ** 2)

# List Comprehension
result = [i ** 2 for i in range(100) if i % 5 == 0]

print(result)


# Tradycyjna metoda
numbers = ["1", "2", "3"]
letters = ["a", "b", "c"]

result = []
for letter in letters:
    for number in numbers:
        result.append(letter + number)

print(result)

# List Comprehension
result = [letter + number for letter in letters for number in numbers]
print(result)

# List Comprehension
# [co ma robić - pętla - warunek]
ls_1 = ["a", "b", "c"]
ls_2 = ["a", "b", "c"]

result = [l_1 + l_2 for l_1 in ls_1 for l_2 in ls_2 if l_1 != l_2]
print(result)

# List Comprehension
# Lista w liście
result = [[j for j in range(10)] for i in range(3)]
print(result)

result = [[(i, j) for j in range(3)] for i in range(2)]
print(result)

result = [[l1 + l2 for l2 in "12345"] for l1 in "abcde"]
print(result)


def silnia(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * silnia(n - 1)


result = [silnia(i) for i in range(7)]
print(result)
