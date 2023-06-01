# Zaimplementuj funkcję o nazwie is_even(), która sprawdzi, czy liczba jest parzysta.
#
#
#
# Przykłady użycia:
#
#
#
# [IN]: is_even(10)
# [OUT]: True
#
#
# [IN]: is_even(13)
# [OUT]: False
#
#
# W tym ćwiczeniu nie dokonujemy żadnej walidacji argumentów. Zakładamy, że użytkownik przekazuje wartości liczbowe.
#
#
#
# Uwaga: Aby zaliczyć ćwiczenie wystarczy zdefiniować funkcję. Nie trzeba jej wywoływać. Zaimplementowane testy sprawdzają poprawność działania funkcji.

def is_even(number):
    return number % 2 == 0