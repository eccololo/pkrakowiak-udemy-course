# Zaimplementuj funkcję o nazwie divisible_by_3_or_5(), która zwraca listę liczb podzielnych przez 3 lub 5 w podanym zakresie (z wartościami krańcowymi włącznie).
#
#
#
# Przykłady użycia:
#
#
#
# [IN]: divisible_by_3_or_5(10, 30)
# [OUT]: [10, 12, 15, 18, 20, 21, 24, 25, 27, 30]
#
#
# [IN]: divisible_by_3_or_5(2, 14)
# [OUT]: [3, 5, 6, 9, 10, 12]
#
#
# W tym ćwiczeniu nie dokonujemy żadnej walidacji argumentów. Zakładamy, że użytkownik przekazuje wartości liczbowe.
#
#
#
# Uwaga: Aby zaliczyć ćwiczenie wystarczy zdefiniować funkcję. Nie trzeba jej wywoływać. Zaimplementowane testy sprawdzają poprawność działania funkcji.


def divisible_by_3_or_5(start, stop):
    return [number for number in range(start, stop + 1) if number % 5 == 0 or number % 3 == 0]
