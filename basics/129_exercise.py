# Zaimplementuj klasę Player, która ma reprezentować piłkarza. Klasa posiadać ma trzy zmienne instancji: name, age i position, które są inicjowane w metodzie konstruktora __init__(). Zaimplementuj również metodę statyczną is_forward(), która przyjmuje pozycję piłkarza i zwraca True, jeśli jest to pozycja ofensywna - 'Striker' lub 'Winger', lub False w przeciwnym razie.
#
#
#
# Uwaga! W celu zaliczenia ćwiczenia należy tylko zaimplementować klasę. Nie trzeba niczego drukować do konsoli. Testy jednostkowe sprawdzają poprawność implementacji rozwiązania.

class Player:

    def __init__(self, name, age, position):
        self.name = name
        self.age = age
        self.position = position

    @staticmethod
    def is_forward(position):
        return position == 'Striker' or position == 'Winger'
