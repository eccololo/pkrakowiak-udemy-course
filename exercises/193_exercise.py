# [IN]: identity(2)
# [OUT]: [[1, 0], [0, 1]]
#
#
# [IN]: identity(3)
# [OUT]: [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
#
#
# [IN]: identity(4)
# [OUT]: [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]


def identity(x):
    my_array = [[0] * x for n in range(x)]
    for idx, item in enumerate(my_array):
        item[idx] = 1
    return my_array


print(identity(4))
