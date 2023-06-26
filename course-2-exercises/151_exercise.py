# Podany jest następujący opis spółki Playway:
#
#
#
# desc = "Playway: Playway to producent gier komputerowych."
#
#
# Zamień wszystkie znaki na małe, usuń dwukropek oraz kropkę i następnie podziel otrzymany tekst na słowa.
#
# Z tak otrzymanej listy utwórz zbiór unikalnych słów. Wydrukuj długość otrzymanego zbioru do konsoli.

desc = "Playway: Playway to producent gier komputerowych."
desc = desc.lower().replace(":", "").replace(".", "").split(" ")
print(set(desc))
