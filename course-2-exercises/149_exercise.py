# Zbuduj generator o nazwie dayname(), który przyjmie indeks elementu poniższej listy:
#
#
#
# days = ['pon', 'wt', 'śr', 'czw', 'pt', 'sb', 'nd']
#
#
# i pozwoli iterować po 3 dniach (dzień wcześniejszy, dzień obecny, dzień następny).

days = ['pon', 'wt', 'śr', 'czw', 'pt', 'sb', 'nd']


def dayname(idx):
    last = idx - 1
    middle = idx
    first = idx + 1
    if last < 0:
        last = 6
    for i in last, middle, first:
        yield days[i]

