# Napisz funkcję calculate_average(), która policzy średnią dowolnej liczby przekazanych argumentów.
#
#
#
# Uwaga: Aby zaliczyć ćwiczenie wystarczy zdefiniować funkcję. Nie trzeba jej wywoływać. Zaimplementowane testy sprawdzają poprawność działania funkcji.


def calculate_average(*args):
    return sum(args) / len(args)
