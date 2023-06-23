# Zaimplementuj klase Substance w ktorej bedziesz mogl obliczyc srednia temperature, z temperatur substancji.

class Substance:
    all_substances = []

    def __init__(self, name, initial_temp):
        self.name = name
        self.temperature = [initial_temp]
        Substance.all_substances.append(self)

    def add_temperature(self, temp):
        self.temperature.append(temp)

    # Enter your solution here
    @classmethod
    def average_temperature(cls):
        total_temp = 0
        len_temp = 0
        for subst in cls.all_substances:
            total_temp += sum(subst.temperature)
            len_temp += len(subst.temperature)

        return total_temp / len_temp

