# Zaimplementuj generator o nazwie enum(), który działa podobnie jak funkcja wbudowana enumerate().
#
# Dla uproszczenia generator ma pobierać obiekt iterowalny i zwracać obiekt typu tuple (indeks, element)

def enum(iter_item):
    counter = 0
    for item in iter_item:
        yield (counter, item)
        counter += 1
