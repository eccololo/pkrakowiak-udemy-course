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
# Zaimplementuj klasę o nazwie Clothing, która będzie dziedziczyć po klasie Product dodając dodatkowe dwa atrybuty: size oraz color.
#
#
#
# Uwaga! W celu zaliczenia ćwiczenia należy tylko zaimplementować klasę. Nie trzeba niczego drukować do konsoli. Testy jednostkowe sprawdzają poprawność implementacji rozwiązania.


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


# Enter your solution here

class Clothing(Product):
    def __init__(self, name, price, size, color):
        super().__init__(name, price)
        self.size = size
        self.color = color