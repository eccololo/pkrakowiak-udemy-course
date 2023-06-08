# Podana
# jest
# poniższa
# klasa
# Soldier:
#
#
# class Soldier:
#     military_count = 0
#
#     def __init__(self, name, rank, years_of_service):
#         self.name = name
#         self.rank = rank
#         self.years_of_service = years_of_service
#         Soldier.military_count += 1
#
#
# Do
# podanej
# klasy
# dodaj
# implementację
# statycznej
# metody
# o
# nazwie
# calculate_years_of_service(), która
# pobiera
# długość
# służby
# wojskowej
# wyrażonej
# w
# dniach
# i
# zwraca
# długość
# służby
# wojskowej
# wyrażonej
# w
# pełnych
# latach
# i
# dniach
# według
# poniższego
# wzorca:
#
# f'{years} year(s), {days} days'
#
# Uwaga! W
# celu
# zaliczenia
# ćwiczenia
# należy
# tylko
# zaimplementować
# metodę.Nie
# trzeba
# niczego
# drukować
# do
# konsoli.Testy
# jednostkowe
# sprawdzają
# poprawność
# implementacji
# rozwiązania.


class Soldier:
    military_count = 0

    def __init__(self, name, rank, years_of_service):
        self.name = name
        self.rank = rank
        self.years_of_service = years_of_service
        Soldier.military_count += 1

    # Enter your solution here
    @staticmethod
    def calculate_years_of_service(days):
        years = days // 365
        days = days % 365
        return f'{years} year(s), {days} days'
