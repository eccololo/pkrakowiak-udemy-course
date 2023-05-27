# Napisz funkcję count_str(), która zwróci liczbę obiektów typu
# str w obiekcie iterowalnym (list, tuple, set).

def count_str(item_iter):
    counter = 0
    for item in item_iter:
        if isinstance(item, str):
            counter += 1

    return counter


print(count_str(["abc", 1, 2, "cbd"]))
