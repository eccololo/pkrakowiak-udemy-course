import math

print("Wartosc bezwzgledna -10 to: ", abs(-10))

print("Pusta lista to w bool: ", bool([]))
print("Spacja w bool to: ", bool(" "))
print("Zero w bool to: ", bool(0))

print("Wszystkie atrybuty i metody listy to: ", dir(list))

print("Funkcja enumerate: ", list(enumerate(["mateusz", "python", "kod"])))

x = 15
print(eval("x + 10"))

# Filter zwraca nam wartosci ktre są True.
print(list(filter(abs, [-2, -1, 0, 1, 2])))
print(list(filter(bool, ["mateusz", "", "python"])))

print(float(1))
print(float(2.5))
print(float("1"))

print(type(1))
print(type("mateusz"))

# help()
# help(float)

print(isinstance(1, int))
print(isinstance("String", str))
print(isinstance(1, float))
print(isinstance("", str))

print(len("mateusz"))
print(len([1, 2, 3, 4]))

print(list("python"))
print(list(range(10)))

# Dzieki funkcji map mozemy zastosowac funkcje abs na kazdym elemencie listy.
print(list(map(abs, [-2, -1, 0, 1, 2])))
print(list(map(str.upper, ["mateusz", "python", "kod"])))

print(max(1, 2, 3, 4, 5, 6))
print(max("mateusz"))

print(min(1, 2, 3, 4, 5, 6))
print(min("mateusz"))

print(pow(2, 4))
print(2 ** 4)

print(list(reversed("mateusz")))
print(list(reversed([1, 2, 3, 4])))

print(round(3.1415, 2))

print(str(1))

print(sum([1, 2, 3, 4]))

lista1 = [1, 2, 3, 4]
lista2 = [5, 6, 7, 8, 9]
lista3 = list(zip(lista1, lista2))
print(lista3)

print(list(zip("python", "kod")))