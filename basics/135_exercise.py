# Załóżmy, że pracujesz nad systemem do obsługi produkcji samolotów pasażerskich. Podana jest poniższa klasa bazowa Component, która ma zaimplementowaną metodę __init__() do ustawiania atrybutów name i weight.
#
#
#
# class Component:
#     def __init__(self, name, weight):
#         self.name = name
#         self.weight = weight
#
#
# Zaimplementuj klasę o nazwie Wing, która będzie dziedziczyć po klasie Component dodając dodatkowy atrybut span.
#
#
#
# Uwaga! W celu zaliczenia ćwiczenia należy tylko zaimplementować klasę. Nie trzeba niczego drukować do konsoli. Testy jednostkowe sprawdzają poprawność implementacji rozwiązania.
#

class Component:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


# Enter your solution here

class Wing(Component):

    def __init__(self, name, weight, span):
        super().__init__(name, weight)
        self.span = span
