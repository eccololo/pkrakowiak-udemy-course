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
# Zaimplementuj w klasie Product następującą metodę:
#
# get_discounted_price() - ta metoda przyjmuje procent rabatu jako argument i zwraca obniżoną cenę produktu o wskazany rabat (metoda nie modyfikuje atrybutu price)
#
#
#
# Przykład użycia metody get_discounted_price():
#
#
#
# [IN]: p = Product('Samsung', 1200, 2)
# [IN]: p.get_discounted_price(20)
# [OUT]: 960.0
#
#
# Uwaga! W celu zaliczenia ćwiczenia należy tylko zaimplementować klasę. Nie trzeba niczego drukować do konsoli. Testy jednostkowe sprawdzają poprawność implementacji rozwiązania.

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    # Enter your solution here

    def get_discounted_price(self, discount):
        return self.price * ((100 - discount) / 100)