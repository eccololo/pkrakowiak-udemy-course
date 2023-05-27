# Napisz funkcję sort_list(), która uporządkuje listę
# składającą się z dwuelementowych obiektów typu tuple według drugiego elementu tupli.

def sort_list(tuple_item):
    return sorted(tuple_item, key=lambda tup: tup[1])


print(sort_list([(1, 3), (4, 1), (4, 2), (0, 7)]))
