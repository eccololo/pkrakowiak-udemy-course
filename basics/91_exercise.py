# Zaimplementuj funkcję o nazwie sort_by_length(), która będzie sortować listę słów według ich długości. Funkcja powinna przyjmować listę słów i zwracać nową posortowaną listę. Do sortowania użyj funkcji wbudowanej sorted() oraz wyrażenia lambda do określenia klucza sortowania.
#
#
#
# Przykłady użycia:
#
#
#
# [IN]: sort_by_length(['apple', 'pear', 'banana', 'pineapple', 'orange'])
# [OUT]: ['pear', 'apple', 'banana', 'orange', 'pineapple']
#
#
# [IN]: sort_by_length(['laptop', 'mouse', 'keyboard', 'screen'])
# [OUT]: ['mouse', 'laptop', 'screen', 'keyboard']
#
#
# W tym ćwiczeniu nie dokonujemy żadnej walidacji argumentów. Zakładamy, że użytkownik przekazuje wartości liczbowe.
#
#
#
# Uwaga: Aby zaliczyć ćwiczenie wystarczy zdefiniować funkcję. Nie trzeba jej wywoływać. Zaimplementowane testy sprawdzają poprawność działania funkcji.

def sort_by_length(words_list):
    return sorted(words_list, key=lambda x: len(x))
