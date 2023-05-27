class Drzewo:

    name = "sosna"
    wiek = 45
    wysokosc = 30

    def __init__(self):
        pass


drzewo_1 = Drzewo()
drzewo_2 = Drzewo()

print(id(drzewo_1))
print(id(drzewo_2))

print(dir(drzewo_1))

print(drzewo_1.name)
print(drzewo_1.wiek)
print(drzewo_1.wysokosc)

drzewo_1.stan = "dobry"

print(dir(drzewo_1))
print(dir(drzewo_2))

Drzewo.miejsce = "las"

print(dir(drzewo_1))
print(dir(drzewo_2))