# Zaimplementuj klase rodzica Product oraz klase dzicko Electronics ktora dziedziczy po Product.
# W klasie Product daj name i price a w klasie dziecka dodaj warranty.


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


# Enter your solution here

class Electronics(Product):
    def __init__(self, warranty, name, price):
        super().__init__(name, price)
        self.warranty = warranty
