def parabola(x):
    return x ** 2 + 3


print(type(parabola))
print(parabola(30))

f = lambda x: x ** 2 + 3
print(f(30))

f2 = lambda word: word.upper()
print(f2("hakunamatata"))

add = lambda x, y: x + y
print(add(10, 20))

f3 = lambda word_1, word_2: word_1 + " " + word_2
print(f3("Hello", "World"))

techs = ["python", "java", "c#", "html", "css", "bootstrap"]
print(list(map(lambda word: word.upper(), techs)))

print(list(map(lambda word: (word, len(word)), techs)))


def apply_function(x, func):
    return func(x)


print(apply_function(5, lambda x: x ** 2))
print(apply_function([15, 45], lambda x: sum(x)))

numbers = [-3, -2, -1, 0, 1, 2, 3]
print(sorted(numbers))
print(sorted(numbers, key=lambda x: abs(x)))

numbers_lang = [("jeden", "one"), ("dwa", "two"), ("trzy", "three")]
print(sorted(numbers_lang))
print(sorted(numbers_lang, key=lambda x: x[1]))
