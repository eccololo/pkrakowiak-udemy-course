# Napisz generator o nazwie geometric_sequence(), który będzie zwracać kolejne liczby z ciągu geometrycznego o zadanym pierwszym wyrazie i ilorazie. Generator powinien działać w nieskończoność, tzn. zwracać kolejne wyrazy ciągu aż do przekroczenia zakresu typu int.
#
#
#
# Przykłady użycia:
#
#
#
# [IN]: geo = geometric_sequence(1, 2)
# [IN]: next(geo)
# [OUT]: 1
# [IN]: next(geo)
# [OUT]: 2
# [IN]: next(geo)
# [OUT]: 4
# [IN]: next(geo)
# [OUT]: 8
# [IN]: next(geo)
# [OUT]: 16
# [IN]: next(geo)
# [OUT]: 32
#
#
# Uwaga: Aby zaliczyć ćwiczenie wystarczy zdefiniować generator. Nie trzeba go wywoływać. Zaimplementowane testy sprawdzają poprawność działania generatora.

def geometric_sequence(wyraz, iloraz):
    n = 1
    while True:
        yield wyraz * (iloraz ** (n - 1))
        n += 1
