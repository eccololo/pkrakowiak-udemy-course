# Napisz funkcję is_distinct(), która sprawdzi, czy lista zawiera unikalne wartości.

def is_distinct(list_item):
    return len(list(set(list_item))) == len(list_item)


print(is_distinct([1, 2, 3]))
print(is_distinct([1, 2, 3, 3]))