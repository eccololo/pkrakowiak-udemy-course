# [IN]: bike1 = MountainBike('Cross', 'Hexagon X-5', 2500, 'full-suspension')
# [IN]: bike1.description()
# [OUT]: 'Mountain bike: Cross Hexagon X-5.'
#
# [IN]: bike2 = RoadBike('Trek', 'Domane', 2000, 32)
# [IN]: bike2.description()
# [OUT]: 'Road bike: Trek Domane.'

class Bike:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def description(self):
        print(f'Bike: {self.brand} {self.model}.')


class MountainBike(Bike):
    def __init__(self, brand, model, price, suspension):
        super().__init__(brand, model, price)
        self.suspension = suspension

    def description(self):
        print(f'Mountain bike: {self.brand} {self.model}.')


class RoadBike(Bike):
    def __init__(self, brand, model, price, tire_width):
        super().__init__(brand, model, price)
        self.tire_width = tire_width

    def description(self):
        print(f'Road bike: {self.brand} {self.model}.')


bike1 = MountainBike('Cross', 'Hexagon X-5', 2500, 'full-suspension')
bike1.description()
# [OUT]: 'Mountain bike: Cross Hexagon X-5.'
