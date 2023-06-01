# Zaimplementuj funkcję o nazwie person_info(), która będzie zwracać opis osoby na podstawie przekazanych do niej argumentów typu klucz-wartość według poniższego schematu:
#
#
#
# f'{name} is {age} years old and lives in {city}.'
#
#
# Funkcja powinna działać dla dowolnej liczby argumentów typu klucz-wartość. Do tego użyj składni **kwargs, która pozwala na przekazywanie zmiennej liczby argumentów typu klucz-wartość do funkcji. Jeśli argument name nie zostanie przekazany ustaw domyślną wartość 'John'. Jeśli jakiś inne argumenty nie zostaną przekazane przy wywołaniu funkcji wstaw wartość <unknown>.
#
#
#
# Przykłady użycia:
#
#
#
# [IN]: person_info(name='John', age=35, city='Los Angeles')
# [OUT]: 'John is 35 years old and lives in Los Angeles.'
#
#
# [IN]: person_info(name='Paul')
# [OUT]: Paul is <unknown> years old and lives in <unknown>.
#
#
# [IN]: person_info(name='Paul', city='Warsaw')
# [OUT]: Paul is <unknown> years old and lives in Warsaw.
#
#
# [IN]: person_info(age=30, city='New York')
# [OUT]: John is 30 years old and lives in New York.
#
#
# W tym ćwiczeniu nie dokonujemy żadnej walidacji argumentów.
#
#
#
# Uwaga: Aby zaliczyć ćwiczenie wystarczy zdefiniować funkcję. Nie trzeba jej wywoływać. Zaimplementowane testy sprawdzają poprawność działania funkcji.

def person_info(**kwargs):
    name = kwargs.get("name", default="<unknown>")
    age = kwargs.get("age", default="<unknown>")
    city = kwargs.get("city", default="<unknown>")
    return f'{name} is {age} years old and lives in {city}.'


person_info(name='Paul')
# [OUT]: Paul is <unknown> years old and lives in <unknown>.
