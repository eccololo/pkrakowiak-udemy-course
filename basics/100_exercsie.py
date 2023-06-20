# [IN]: geo = geometric_sequence(1, 2)
# [IN]: next(geo)
# [OUT]: 1
# [IN]: next(geo)
# [OUT]: 2
# [IN]: next(geo)
# [OUT]: 4
# [IN]: next(geo)
# [OUT]: 8
# [IN]: next(geo)
# [OUT]: 16
# [IN]: next(geo)
# [OUT]: 32

def geometric_sequence(wyraz, iloraz):
    n = 1
    while True:
        yield wyraz * (iloraz ** (n - 1))
        n += 1
