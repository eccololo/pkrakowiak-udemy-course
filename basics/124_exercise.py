# Załóżmy, że pracujesz nad projektem e-commerce. Masz już utworzoną klasę o nazwie Product reprezentującą produkt w asortymencie sklepu internetowego:
#
#
#
# class Product:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#
#
# Zaimplementuj w klasie Product dwie metody umożliwiające użytkownikowi aktualizację ceny i ilości produktu odpowiednio o nazwach:
#
# update_price()
#
# update_quantity()
#
#
#
# Uwaga! W celu zaliczenia ćwiczenia należy tylko zaimplementować klasę. Nie trzeba niczego drukować do konsoli. Testy jednostkowe sprawdzają poprawność implementacji rozwiązania.

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    # Enter your solution here

    def update_price(self, new_price):
        self.price = new_price

    def update_quantity(self, new_quantity):
        self.quantity = new_quantity