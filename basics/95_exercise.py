# Zaimplementuj funkcję o nazwie count_kwargs(), która będzie zwracać liczbę przekazanych argumentów typu klucz-wartość (keyword arguments) do funkcji.
#
#
#
# Przykłady użycia:
#
#
#
# [IN]: count_kwargs(a=1, b=3)
# [OUT]: 2
#
#
# [IN]: count_kwargs(10, 'John', age=20, country='USA')
# [OUT]: 2
#
#
# [IN]: count_kwargs(30, 1)
# [OUT]: 0
#
#
# [IN]: count_kwargs()
# [OUT]: 0
#
#
# W tym ćwiczeniu nie dokonujemy żadnej walidacji argumentów.
#
#
#
# Uwaga: Aby zaliczyć ćwiczenie wystarczy zdefiniować funkcję. Nie trzeba jej wywoływać. Zaimplementowane testy sprawdzają poprawność działania funkcji.

def count_kwargs(**kwargs):
    return len(kwargs)