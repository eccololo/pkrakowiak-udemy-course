techs = {"java", "python", "java"}

print(techs)
print(len(techs))

print(set("python"))
print(set("aaaaale"))

techs.add("c++")

print(techs)
techs.remove("java")
print(techs)

techs.pop()
print(techs)

A = {1, 2, 3, 4, 5, 6, 7}
B = {4, 5, 6, 7, 8}
C = {5, 6}

# Czy jest podzbiorem i czy jest nadzbiorem.
print(C.issubset(A))
print(A.issuperset(C))

# Suma zbiorow
print(A.union(B))

# Czesc wspolna zbiorow
print(A.intersection(B))

# Roznica zbiorow A i B plus roznica zbiorow B i A
print(A.symmetric_difference(B))

# kopiowanie zbioru
D = A.copy()
D.pop()
print(D)
print(A)