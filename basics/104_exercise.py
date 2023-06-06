# Załóżmy, że masz listę słowników, z których każdy reprezentuje produkt w twoim sklepie e-commerce. Każdy produkt posiada nazwę, cenę oraz ilość dostępną na magazynie:
#
#
#
# products = [
#     {'name': 'T-shirt', 'price': 20, 'quantity': 10},
#     {'name': 'Jeans', 'price': 50, 'quantity': 0},
#     {'name': 'Sneakers', 'price': 80, 'quantity': 5},
#     {'name': 'Hat', 'price': 15, 'quantity': 3},
#     {'name': 'Backpack', 'price': 30, 'quantity': 7}
# ]
#
#
# Chcesz utworzyć nową listę o nazwie in_stock zawierającą tylko nazwy produktów, które są aktualnie w magazynie (tj. quantity > 0). Do rozwiązania tego problemu wykorzystaj list comprehension. W odpowiedzi wydrukuj do konsoli listę in_stock.
#
#
#
# Oczekiwany wynik:
#
#
#
# ['T-shirt', 'Sneakers', 'Hat', 'Backpack']

products = [
    {'name': 'T-shirt', 'price': 20, 'quantity': 10},
    {'name': 'Jeans', 'price': 50, 'quantity': 0},
    {'name': 'Sneakers', 'price': 80, 'quantity': 5},
    {'name': 'Hat', 'price': 15, 'quantity': 3},
    {'name': 'Backpack', 'price': 30, 'quantity': 7}
]

in_stock = [dict_item["name"] for dict_item in products if dict_item["quantity"] > 0]

print(in_stock)
