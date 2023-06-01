# Zaimplementuj funkcję o nazwie create_dictionary(), która będzie tworzyć słownik z przekazanych do niej argumentów typu klucz-wartość. Funkcja powinna działać dla dowolnej liczby argumentów. Do tego użyj składni **kwargs, która pozwala na przekazywanie zmiennej liczby argumentów typu klucz-wartość do funkcji.
#
#
#
# Przykłady użycia:
#
#
#
# [IN]: create_dictionary(age=20, name='Mike')
# [OUT]: {'age': 20, 'name': 'Mike'}
#
#
# [IN]: create_dictionary(level='senior', stack=['python', 'aws', 'sql'])
# [OUT]: {'level': 'senior', 'stack': ['python', 'aws', 'sql']}
#
#
# [IN]: create_dictionary(country='Poland')
# [OUT]: {'country': 'Poland'}
#
#
# W tym ćwiczeniu nie dokonujemy żadnej walidacji argumentów.
#
#
#
# Uwaga: Aby zaliczyć ćwiczenie wystarczy zdefiniować funkcję. Nie trzeba jej wywoływać. Zaimplementowane testy sprawdzają poprawność działania funkcji.

def create_dictionary(**kwargs):
    return {key: value for (key, value) in kwargs.items()}
