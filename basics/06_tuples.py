moja_tupla = tuple()
print(moja_tupla)

allegro_tupla = ("Allegro", "Polska", "Sprzedaz", 1)
google_tuple = ("Google", "USA", "Technologia", 2)
print(allegro_tupla)

google_name = google_tuple[0]
print(google_name)

data = (allegro_tupla, google_tuple)
print(data)

imie, nazwisko = ("Mateusz", "Hyla")
print(imie, nazwisko)

nazwa, kraj, branza, rank = allegro_tupla
print(nazwa, kraj, branza, rank)

a = 10
b = 20

c = b
b = a
a = c

print(a, b)

x, y = 10, 20
x, y = y, x
print(x, y)