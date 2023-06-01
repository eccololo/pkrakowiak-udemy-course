# Podana jest lista miast:
#
#
#
# cities = ['Warsaw', 'London', 'Berlin', 'New York']
#
#
# Używając funkcji map() oraz wyrażenia lambda uzyskaj listę zawierającą trzy pierwsze litery każdego miasta. Otrzymaną listę wydrukuj do konsoli.
#
#
#
# Oczekiwany wynik:
#
#
#
# ['War', 'Lon', 'Ber', 'New']

cities = ['Warsaw', 'London', 'Berlin', 'New York']

output = list(map(lambda x: x[:3], cities))
print(output)