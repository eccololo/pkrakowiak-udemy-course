# Załóżmy, że
# pracujesz
# nad
# projektem
# e - commerce.Masz
# już
# utworzoną
# klasę
# o
# nazwie
# Product
# reprezentującą
# produkt
# w
# asortymencie
# sklepu
# internetowego:
#
#
# class Product:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#
#     def update_price(self, new_price):
#         self.price = new_price
#
#     def update_quantity(self, new_quantity):
#         self.quantity = new_quantity
#
#
# Zaimplementuj
# w
# klasie
# Product
# następujące
# metody:
#
# get_total_price() - ta
# metoda
# oblicza
# i
# zwraca
# całkowitą
# cenę
# produktu
# na
# podstawie
# ilości
# i
# ceny
#
# is_in_stock() - ta
# metoda
# zwraca
# wartość
# logiczną
# wskazującą, czy
# produkt
# jest
# w
# magazynie, czy
# nie
#
# Uwaga! W
# celu
# zaliczenia
# ćwiczenia
# należy
# tylko
# zaimplementować
# klasę.Nie
# trzeba
# niczego
# drukować
# do
# konsoli.Testy
# jednostkowe
# sprawdzają
# poprawność
# implementacji
# rozwiązania.

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def update_price(self, new_price):
        self.price = new_price

    def update_quantity(self, new_quantity):
        self.quantity = new_quantity

    # Enter your solution here

    def get_total_price(self):
        return self.price * self.quantity

    def is_in_stock(self):
        return self.quantity > 0
