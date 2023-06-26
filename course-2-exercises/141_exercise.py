# Podana jest lista:
#
#
#
# items = [(3, 4), (2, 5), (1, 4), (6, 1)]
#
#
# Posortuj listę według rosnącej sumy kwadratów liczb podanych
# w obiektach typu tuple. Użyj metody list.sort() oraz wyrażenia
# lambda. W odpowiedzi wydrukuj listę do konsoli.

items = [(3, 4), (2, 5), (1, 4), (6, 1)]

list.sort(items, key=lambda tup: tup[0] ** 2 + tup[1] ** 2)
print(items)
