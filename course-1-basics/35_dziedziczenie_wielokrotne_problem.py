class A:

    def metoda(self):
        print("Metoda z klasy A")


class B(A):
    pass
    # def metoda(self):
    #     print("Metoda z klasy B")


class C(A):
    pass
    # def metoda(self):
    #     print("Metoda z klasy C")


class D(B, C):
    pass
    # def metoda(self):
    #     print("Metoda z klasy D")


d = D()
d.metoda()