# Załóżmy, że pracujesz nad projektem kosmicznym i otrzymujesz listę gwiazd wraz z ich odległościami od Ziemi w latach świetlnych:
#
#
#
# stars = [
#     ('Alpha Centauri', 4.37),
#     ('Barnard\'s Star', 5.96),
#     ('Wolf 359', 7.78),
#     ('Lalande 21185', 8.29),
#     ('Sirius A', 8.6),
#     ('Sirius B', 8.6),
#     ('Luyten 726-8 A', 8.73),
#     ('Luyten 726-8 B', 8.73),
#     ('Ross 154', 9.69),
#     ('Ross 248', 10.32),
# ]
#
#
# Twoim zadaniem jest stworzenie zbioru wszystkich gwiazd znajdujących się bliżej niż 8 lat świetlnych od Ziemi. Otrzymany zbiór przypisz do zmiennej close_stars.
#
#
#
# Oczekiwana postać zbioru:
#
#
#
# {"Barnard's Star", 'Alpha Centauri', 'Wolf 359'}
#
#
# Uwaga! Wystarczy tylko utworzyć zbiór. Nie trzeba go drukować do konsoli.

stars = [
    ('Alpha Centauri', 4.37),
    ('Barnard\'s Star', 5.96),
    ('Wolf 359', 7.78),
    ('Lalande 21185', 8.29),
    ('Sirius A', 8.6),
    ('Sirius B', 8.6),
    ('Luyten 726-8 A', 8.73),
    ('Luyten 726-8 B', 8.73),
    ('Ross 154', 9.69),
    ('Ross 248', 10.32),
]

# Enter your solution here

close_stars = {star[0] for star in stars if star[1] < 8}

print(close_stars)