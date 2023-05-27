# [IN]: top_n([4, 5, 2, 9, 5, 2, 8, 2, 8, 10], 3)
# [OUT]: [10, 9, 8]

# def top_n(lista, n):
#     maks = 0
#     output_list = []
#     indeks = 0
#     indeksy_to_delete = []
#
#     for _ in range(n):
#         maks = 0
#         for idx, item in enumerate(lista):
#             if item > maks:
#                 maks = item
#                 indeks = idx
#         indeksy_to_delete.append(indeks)
#
#     for item in indeksy_to_delete:
#         output_list.append(lista[item])
#
#     return output_list

def top_n(lista, n):
    lista.sort(reverse=True)
    return lista[:n]


print(top_n([4, 5, 2, 9, 5, 2, 8, 2, 8, 10], 3))
