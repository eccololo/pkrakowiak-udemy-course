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
# Z listy stocks wyciągnij spółki z indeksu 'mWIG40' w postaci listy i wynik wydrukuj do konsoli.

stocks = [
    {'indeks': 'mWIG40', 'name': 'TEN', 'price': 304},
    {'indeks': 'mWIG40', 'name': 'PLW', 'price': 309},
    {'indeks': 'sWIG80', 'name': 'BBT', 'price': 22}
]

output_list = list(filter(lambda d: d["indeks"] == "mWIG40", stocks))

print(output_list)
