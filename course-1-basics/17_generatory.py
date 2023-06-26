def generator():
    yield 4
    yield 5


gen = generator()

print(next(gen))
print(next(gen))


def generator_2(word):
    letters = list(word)
    for char in letters:
        yield char


gen_2 = generator_2("python")
print(next(gen_2))
print(next(gen_2))

for item in generator_2("niebo"):
    print(item)

files = ["script1.py", "script2.py", "plik.txt"]


def files_gen(lista):
    for file_name in lista:
        if file_name.endswith(".py"):
            yield file_name


gen_f = files_gen(files)

# print(next(gen_f))
# print(next(gen_f))
# print(next(gen_f))

for i in gen_f:
    print(i)