# Napisz program, który wczytuje ten plik tekstowy, przetwarza te dane
# i oblicza całkowitą energię wygenerowaną przez elektrownię wiatrową
# (druga kolumna pliku, energia wyrażona w MW). Wynik wydrukuj do konsoli tak jak pokazano poniżej.

with open("72_data.txt", "r") as f:
    suma = 0
    for line in f:
        line = line.replace("\n", "")
        print(line)
        suma += float(line.split(",")[1])

print(f"Total power generated: {round(suma, 2)}0 MW")