# [IN]: trace([[1]])
# [OUT]: 1
#
#
# [IN]: trace([[1, 2], [4, 2]])
# [OUT]: 3
#
#
# [IN]: trace([[3, 4, 5], [5, 2, 1], [5, 7, 2]])
# [OUT]: 7

def trace(macierz):
    suma = 0
    if len(macierz) == 1:
        return macierz[0][0]

    for idx, item in enumerate(macierz):
        suma += item[idx]

    return suma


print(trace([[1, 2], [4, 2]]))
