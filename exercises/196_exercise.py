# [IN]: transpose([[1, 2, 3], [4, 5, 6]])
# [OUT]: [[1, 4], [2, 5], [3, 6]]
#
#
# [IN]: transpose([[1, 2], [3, 4], [5, 6]])
# [OUT]: [[1, 3, 5], [2, 4, 6]]
#
#
# [IN]: transpose([[1, 2, 3, 4], [5, 6, 7, 8]])
# [OUT]: [[1, 5], [2, 6], [3, 7], [4, 8]]


def transpose(macierz):
    partial_list = []
    for idx_i, item in enumerate(macierz):
        for idx_y, i in enumerate(item):
            if idx_i == 0:
                partial_list.append([i])
            else:
                partial_list[idx_y].append(i)

    return partial_list


print(transpose([[1, 2], [3, 4], [5, 6]]))
