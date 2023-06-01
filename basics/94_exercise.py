# Zaimplementuj funkcję o nazwie join_strings(), która będzie łączyć przekazane do niej ciągi znaków w jeden długi ciąg znaków. Pomiędzy argumentami funkcji wstaw znak spacji - ' '. Funkcja powinna działać dla dowolnej liczby argumentów. Do tego użyj składni *args, która pozwala na przekazywanie zmiennej liczby argumentów do funkcji.
#
#
#
# Przykłady użycia:
#
#
#
# [IN]: join_strings('this', 'is', 'an', 'example')
# [OUT]: 'this is an example'
#
#
# [IN]: join_strings('Python', 'is', 'awesome')
# [OUT]: 'Python is awesome'
#
#
# [IN]: join_strings()
# [OUT]: ''
#
#
# W tym ćwiczeniu nie dokonujemy żadnej walidacji argumentów. Zakładamy, że użytkownik przekazuje poprawne wartości.
#
#
#
# Uwaga: Aby zaliczyć ćwiczenie wystarczy zdefiniować funkcję. Nie trzeba jej wywoływać. Zaimplementowane testy sprawdzają poprawność działania funkcji.


def join_strings(*args):
    return " ".join(args)