# Napisz funkcję remove_duplicates(),
# która usunie duplikaty z listy (kolejność elementów nie musi być zachowana).

def remove_duplicates(item_list):
    return list(set(item_list))


print(remove_duplicates([1, 5, 3, 2, 2, 4, 2, 4]))
