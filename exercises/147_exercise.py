# Zbuduj generator o nazwie file_gen(), który z otrzymanej listy
# z nazwami plików, wybierze tylko te z rozszerzeniem .txt.

def file_gen(list_item):
    for item in list_item:
        if item.endswith(".txt"):
            yield item
