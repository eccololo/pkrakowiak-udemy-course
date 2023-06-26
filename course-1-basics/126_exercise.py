# [IN]: p = Product('Samsung', 1200, 2)
# [IN]: p.get_discounted_price(20)
# [OUT]: 960.0

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    # Enter your solution here

    def get_discounted_price(self, discount):
        return self.price * ((100 - discount) / 100)