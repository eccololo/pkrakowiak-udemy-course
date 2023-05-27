from rocket.data import get_data

print(get_data())

import rocket.algorytmy as ra

print(dir(ra))

ra.drzewa_decyzyjne()
ra.sieci_neuronowe()

from rocket.funkcje.stats import mean

print(mean([1, 2, 3]))
