# Max Prob

# [IN]: max_prob([[0.3, 0.4, 0.3], [0.0, 0.1, 0.9]])
# [OUT]: [[0.4], [0.9]]
#
#
# [IN]: max_prob([[0.3, 0.4, 0.2, 0.1], [0.0, 0.1, 0.7, 0.2]])
# [OUT]: [[0.4], [0.7]]
#
#
# [IN]: max_prob([[0.3, 0.4, 0.2, 0.1], [0.0, 0.1, 0.7, 0.2], [0.0, 0.4, 0.3, 0.3]])
# [OUT]: [[0.4], [0.7], [0.4]]

# Detect class

# [IN]: detect_class([[0.3, 0.4, 0.2, 0.1], [0.0, 0.1, 0.7, 0.2]])
# [OUT]: [[0, 1, 0, 0], [0, 0, 1, 0]]
#
#
# [IN]: detect_class([[0.3, 0.4, 0.2, 0.1], [0.0, 0.1, 0.7, 0.2], [0.0, 0.3, 0.3, 0.4]])
# [OUT]: [[0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]


def max_prob(macierz):
    output_list = []

    for item in macierz:
        output_list.append([max(item)])

    return output_list


def detect_class(macierz):
    output_list = []
    maks = 0
    indeks = 0

    for idx_i, item in enumerate(macierz):
        maks = 0
        indeks = 0
        for idx_y, i in enumerate(item):
            if i > maks:
                maks = i
                indeks = idx_y
        item[indeks] = 1

    for item in macierz:
        for idx, i in enumerate(item):
            if i != 1:
                item[idx] = 0

    return macierz


# print(max_prob([[0.3, 0.4, 0.3], [0.0, 0.1, 0.9]]))

print(detect_class([[0.3, 0.4, 0.2, 0.1], [0.0, 0.1, 0.7, 0.2], [0.0, 0.3, 0.3, 0.4]]))
