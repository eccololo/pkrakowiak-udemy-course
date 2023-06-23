# Zaimplementuj klase rodzica Component oraz klase dzicko Wing ktora dziedziczy po Component.
# W klasie Component daj name i weight a w klasie dziecka dodaj span.

class Component:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


# Enter your solution here

class Wing(Component):

    def __init__(self, name, weight, span):
        super().__init__(name, weight)
        self.span = span
