# Podana jest poniższa lista:
#
#
#
# stocks = [
#     {'indeks': 'mWIG40', 'name': 'TEN', 'price': 304},
#     {'indeks': 'mWIG40', 'name': 'PLW', 'price': 309},
#     {'indeks': 'sWIG80', 'name': 'BBT', 'price': 22}
# ]
#
#
# Przekształć podaną listę na listę wartości logicznych (True, False).
# True w przypadku, gdy spółka należy do indeksu 'mWIG40', False przeciwnie.
# Przekształconą listę wydrukuj do konsoli.

stocks = [
    {'indeks': 'mWIG40', 'name': 'TEN', 'price': 304},
    {'indeks': 'mWIG40', 'name': 'PLW', 'price': 309},
    {'indeks': 'sWIG80', 'name': 'BBT', 'price': 22}
]

output_list = list(map(lambda d: d["indeks"] == 'mWIG40', stocks))

print(output_list)