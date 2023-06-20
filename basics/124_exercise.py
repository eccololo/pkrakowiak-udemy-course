# Stworz klase o nazwie Product. W konstruktorze zainicjuj zmienne o nazwie name, price i quantity.
# Utworz settery dla price i quantity.

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