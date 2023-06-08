# Podana jest poniższa klasa bazowa Product, która ma zaimplementowaną metodę __init__() do ustawiania atrybutów name i price.
#
#
#
# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#
# Zaimplementuj klasę o nazwie Electronics, która będzie dziedziczyć po klasie Product dodając dodatkowy atrybut warranty.
#
#
#
# Uwaga! W celu zaliczenia ćwiczenia należy tylko zaimplementować klasę. Nie trzeba niczego drukować do konsoli. Testy jednostkowe sprawdzają poprawność implementacji rozwiązania.
#


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


# Enter your solution here

class Electronics(Product):
    def __init__(self, warranty, name, price):
        super().__init__(name, price)
        self.warranty = warranty
