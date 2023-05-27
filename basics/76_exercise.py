# Podany
# jest
# poniższy
# słownik
# zawierający
# dane
# giełdowe:
#
# stock_data = {
#     'AAPL': 145.9,
#     'GOOG': 2680.7,
#     'TSLA': 712.6,
#     'AMZN': 3379.1
# }
#
# Zapisz
# te
# dane
# do
# pliku
# tekstowego
# stock_prices.txt.Każdą
# spółkę
# zapisz
# jako
# wiersz, który
# składa
# się
# z
# nazwy
# spółki
# i
# ceny
# akcji, oddzielonych
# średnikiem.Każdy
# wiersz
# zakończ
# znakiem
# nowej
# linii \n.
#
# Zawartość
# pliku
# stock_prices.txt
# po
# zapisaniu
# danych:
#
# AAPL;
# 145.9
# GOOG;
# 2680.7
# TSLA;
# 712.6
# AMZN;
# 3379.1

stock_data = {
    'AAPL': 145.9,
    'GOOG': 2680.7,
    'TSLA': 712.6,
    'AMZN': 3379.1
}

with open("76_stock_prices.txt", "w") as f:
    for key, value in stock_data.items():
        f.write(f"{key};{value}\n")
