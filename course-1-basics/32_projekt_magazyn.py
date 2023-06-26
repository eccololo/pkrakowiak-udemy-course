import sys

class Magazyn:

    def __init__(self, lista_produktow):
        self.lista_produktow = lista_produktow

    def wyswietl_dostepne_produkty(self):
        print("Dostępne produkty: ")
        for produkt in self.lista_produktow:
            print(produkt)

    def dodaj_produkt(self):
        self.nazwa_produktu = input("Podaj nazwę produktu: >>> ")
        if self.nazwa_produktu not in self.lista_produktow:
            self.lista_produktow.append(self.nazwa_produktu)

        print(f"Produkt {self.nazwa_produktu} zostal dodany do magazynu.")

    def usun_produkt(self):
        self.nazwa_produktu = input("Podaj nazwę produktu ktory chcesz usunac: >>> ")
        if self.nazwa_produktu in self.lista_produktow:
            self.lista_produktow.remove(self.nazwa_produktu)
            print("Usunieto produkt z magazynu.")
        else:
            print("Podanego produktu nie ma w magazynie.")


magazyn = Magazyn(["mleko", "woda", "jajka", "pomidor", "ogorek"])

while True:
    print("1 -  Stan Magazynu.")
    print("2 -  Dodawanie Produktu.")
    print("3 -  Usuwanie Produktu.")
    print("4 -  Exit.")

    user_choice = int(input(">>> "))
    if user_choice == 1:
        magazyn.wyswietl_dostepne_produkty()
    elif user_choice == 2:
        magazyn.dodaj_produkt()
    elif user_choice == 3:
        magazyn.usun_produkt()
    elif user_choice == 4:
        print("Program terminated! Bye!")
        sys.exit()
