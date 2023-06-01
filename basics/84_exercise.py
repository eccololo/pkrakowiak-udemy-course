# Podana jest poniższa lista:
#
#
#
# values = ['5', '2', '8', '1', '9', '3']
#
#
# Używając funkcji wbudowanej map() dokonaj konwersji elementów listy na typ int. Otrzymaną listę wydrukuj do konsoli.
#
#
#
# Oczekiwany wynik:
#
#
#
# [5, 2, 8, 1, 9, 3]

values = ['5', '2', '8', '1', '9', '3']
output = list(map(lambda x: int(x), values))
print(output)