# [IN]: dot_product([1, 2], [5, 2])
# [OUT]: 9


def dot_product(list1, list2):
    suma = 0
    partial_list = []

    for item in zip(list1, list2):
        iloczyn = item[0] * item[1]
        suma += iloczyn

    return suma


print(dot_product([1, 2], [5, 2]))