# Zaimplementuj funkcję o nazwie multiply(), która będzie zwracać iloczyn wszystkich przekazanych do niej argumentów. Funkcja powinna działać dla dowolnej liczby argumentów. Do tego użyj składni *args, która pozwala na przekazywanie zmiennej liczby argumentów do funkcji.
#
#
#
# Przykłady użycia:
#
#
#
# [IN]: multiply(4, 2)
# [OUT]: 8
#
#
# [IN]: multiply(4, 3, 2)
# [OUT]: 24
#
#
# [IN]: multiply(4, 3, 2)
# [OUT]: None
#
#
# W tym ćwiczeniu nie dokonujemy żadnej walidacji argumentów. Zakładamy, że użytkownik przekazuje wartości liczbowe.
#
#
#
# Uwaga: Aby zaliczyć ćwiczenie wystarczy zdefiniować funkcję. Nie trzeba jej wywoływać. Zaimplementowane testy sprawdzają poprawność działania funkcji.

def multiply(*args):
    if len(args) == 0:
        return None
    output = 1
    for i in args:
        output *= i
    return output


print(multiply(4, 2))
print(multiply(4, 3, 2))
