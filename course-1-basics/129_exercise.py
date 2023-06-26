# Zaimplementuj klase Player ktora zwroci True jesli gracz gra na pozycji Striker lub Winger.
# Jesli nie to False.

class Player:

    def __init__(self, name, age, position):
        self.name = name
        self.age = age
        self.position = position

    @staticmethod
    def is_forward(position):
        return position == 'Striker' or position == 'Winger'
