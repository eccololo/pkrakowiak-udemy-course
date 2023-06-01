# Napisz funkcję calculate_average() która przyjmie trzy argumenty i zwróci ich średnią wartość.
#
#
#
# W tym ćwiczeniu nie dokonujemy żadnej walidacji argumentów. Zakładamy, że użytkownik przekazuje wartości liczbowe.
#
#
#
# Uwaga: Aby zaliczyć ćwiczenie wystarczy zdefiniować funkcję. Nie trzeba jej wywoływać. Zaimplementowane testy sprawdzają poprawność działania funkcji.

def calculate_average(*args):
    return sum(args) / len(args)