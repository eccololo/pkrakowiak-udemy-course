# [IN]:  [
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

# [OUT]: {"Barnard's Star", 'Alpha Centauri', 'Wolf 359'}

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