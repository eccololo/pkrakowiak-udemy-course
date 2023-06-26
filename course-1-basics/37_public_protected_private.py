# public - zmienna
# protected - _zmienna
# private - __zmienna

class Spolka:

    def __init__(self, rodzaj, rynek, gielda):
        self.rodzaj = rodzaj
        self._rynek = rynek
        self__gielda = gielda


class KGHM(Spolka):

    def __init__(self, rodzaj, rynek, gielda, nazwa):
        super().__init__(rodzaj, rynek, gielda)
        self.nazwa = nazwa

        print(f"Artybut publiczny: {self.rodzaj}")
        print(f"Artybut protected: {self._rynek}")
        # print(f"Artybut private: {self.__gielda}")


spolka = Spolka("Spolka Akcyjna", "Główny", "GPW w Warszawie")
print(f"Artybut publiczny: {spolka.rodzaj}")
print(f"Artybut protected: {spolka._rynek}")
# print(f"Artybut private: {spolka.__gielda}")

kghm = KGHM("Spolka Akcyjna", "Główny", "GPW w Warszawie", "KGHM")
# print(f"Artybut private: {kghm._Spolka__gielda}")
