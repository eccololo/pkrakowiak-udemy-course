# Załóżmy, że pracujesz nad projektem, który obejmuje analizę danych z elektrowni słonecznej. Masz listę krotek reprezentujących dzienną produkcję energii:
#
#
#
# data = [(1, 20), (2, 15), (3, 25), (4, 18), (5, 22), (6, 21)]
#
#
# Każda krotka zawiera dwie wartości: pierwsza wartość to dzień miesiąca, a druga wartość to ilość energii wyprodukowanej przez elektrownię w kilowatogodzinach (kWh). Potrzebujesz znaleźć zbiór wszystkich dni, w których elektrownia wyprodukowała co najmniej 20 kWh energii. Otrzymany zbiór przypisz do zmiennej output_set.
#
#
#
# Uwaga! Wystarczy tylko utworzyć zbiór. Nie trzeba go drukować do konsoli.

data = [(1, 20), (2, 15), (3, 25), (4, 18), (5, 22), (6, 21)]

# Enter your solution here

output_set = {item[0] for item in data if item[1] >= 20}

print(output_set)