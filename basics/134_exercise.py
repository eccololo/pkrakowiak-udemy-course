# Zaimplementuj klase rodzica Product oraz klase dzicko Clothing ktora dziedziczy po Product.
# W klasie Product daj name i price a w klasie dziecka dodaj size, color.

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