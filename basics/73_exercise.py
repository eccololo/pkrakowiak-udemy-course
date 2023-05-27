# Napisz program, który wczytuje ten plik CSV, przetwarza te dane i
# oblicza średnią energię wygenerowaną przez elektrownię wodną
# (trzecia kolumna pliku, energia wyrażona w kWh).
# Wynik wydrukuj do konsoli tak jak pokazano poniżej.

with open("73_data.csv", "r") as f:
    data = f.readlines()

suma = 0
for idx, line in enumerate(data):
    if idx == 0:
        continue
    line = line.replace("\n", "")
    suma += float(line.split(",")[2])

average = suma / (len(data) - 1)

print(f"Average energy generated: {average:.2f} kWh")
