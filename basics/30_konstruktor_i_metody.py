class Drzewo:


    def __init__(self, nazwa, wiek, wysokosc):
        self.nazwa = nazwa
        self.wiek = wiek
        self.wysokosc = wysokosc

    def czy_chronione(self):
        if self.wiek > 20 and self.wysokosc > 30:
            print(f"To drzewo {self.nazwa} jest chronione.")
        else:
            print(f"To drzewo {self.nazwa} nie jest chronione.")

    def postarz_o_rok(self):
        self.wiek += 1


drzewo_1 = Drzewo("Sosna", 35, 25)
drzewo_2 = Drzewo("Brzoza", 25, 45)
print(drzewo_1.nazwa)
print(drzewo_2.nazwa)

drzewo_1.czy_chronione()
drzewo_2.czy_chronione()

print(drzewo_1.wiek)
drzewo_1.postarz_o_rok()
print(drzewo_1.wiek)

