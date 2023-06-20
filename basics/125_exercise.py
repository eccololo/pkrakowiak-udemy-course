# Stworz klase o nazwie Product. W konstruktorze zainicjuj zmienne o nazwie name, price i quantity.
# Utworz settery dla price i quantity.
# Utworz dwie dodatkowe metody:
# 1. metoda ktora zwroci nam cene całkowitą produktow
# 2. metode ktora zwroci True lub False w zaleznosci czy sa jakiej produkty w magazynie

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
