print(int.__add__(1, 2))
print(int.__sub__(5, 10))
print(int.__lt__(3, 5))


class SpecialInt(int):

    def __init__(self, special_int):
        self.special_int = special_int

    def __add__(self, other):
        return self.special_int + other.special_int + 10

    def __sub__(self, other):
        return self.special_int - other.special_int - 10


s1 = SpecialInt(1)
s2 = SpecialInt(4)

print(s1 + s2)
print(s1 - s2)


class Kwadrat:

    def __init__(self, dlugosc_boku):
        self.db = dlugosc_boku

    def __str__(self):
        return f"Kwadrat o boku {self.db} cm."

    def pole(self):
        return self.db ** 2

    def __add__(self, other):
        return self.pole() + other.pole()

    def __sub__(self, other):
        return self.pole() - other.pole()

    def __lt__(self, other):
        return self.pole() < other.pole()


k1 = Kwadrat(3)
print(k1)

k2 = Kwadrat(10)
print(k2)

print(k1 + k2)
print(k1 - k2)
print(k1 < k2)
