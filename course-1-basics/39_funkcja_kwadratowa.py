import numpy as np


class FunkcjaKwadratowa:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def make_function(self):
        print(f"{self.a} * x ** 2 + {self.b} * x + {self.c}")

    def rozwiaz(self):
        if self.a == 0 and self.b == 0 and self.c == 0:
            print("Równanie tożsamościowe.")
        elif self.a == 0 and self.b == 0 and self.c != 0:
            print("Równanie sprzeczne.")
        elif self.a == 0 and self.b != 0:
            x = - self.c / self.b
            print(x)
        elif self.a != 0:
            delta = self.b ** 2 - (4 * self.a * self.c)
            if delta > 0:
                sqrt_delta = np.sqrt(delta)
                x1 = (- self.b - sqrt_delta) / (self.a * 2)
                x2 = (- self.b + sqrt_delta) / (self.a * 2)
                print(x1, x2)
            elif delta == 0:
                x = - self.b / (self.a * 2)
                print(x)
            else:
                print("Brak rozwiązań.")
        else:
            raise ValueError


fk = FunkcjaKwadratowa(3, 1, 4)
fk.make_function()
fk.rozwiaz()


def main():
    for i in range(1000):
        a = np.random.choice(range(-100, 100))
        b = np.random.choice(range(-100, 100))
        c = np.random.choice(range(-100, 100))
        fk = FunkcjaKwadratowa(a, b, c)
        fk.rozwiaz()


if __name__ == '__main__':
    main()
