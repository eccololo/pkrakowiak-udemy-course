# Zaimplementuj klasy Component, Wing, Engine oraz Plane.
# Wing i Engine dziedziczy po Component.
# W plane daj mozliwosc dodania komponentow jak Wind i Engine oraz oblicz wage samolotu.
# Component ma name oraz weight.
# Wing ma dodatkowo span.
# Engine ma dodatkowo power.
# Dodaj w Plane mozliwosc obliczenia ratio power do weight


class Component:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


class Wing(Component):
    def __init__(self, name, weight, span):
        super().__init__(name, weight)
        self.span = span


class Engine(Component):
    def __init__(self, name, weight, power):
        super().__init__(name, weight)
        self.power = power


class Plane:
    def __init__(self, name):
        self.name = name
        self.components = []

    def add_component(self, component):
        self.components.append(component)

    def calculate_weight(self):
        total_weight = 0
        for component in self.components:
            total_weight += component.weight
        return total_weight

    def calculate_power_to_weight_ratio(self):
        total_power = 0
        for component in self.components:
            if isinstance(component, Engine):
                total_power += component.power
        return total_power / self.calculate_weight()


# Enter your solution here

plane = Plane("Boeing 747")
r_wing = Wing('Right Wing', 1200, 15)
l_wing = Wing('Left Wing', 1200, 15)
engine = Engine('Turbofan Engine', 3500, 20000)
plane.add_component(r_wing)
plane.add_component(l_wing)
plane.add_component(engine)

print(plane.calculate_weight())

