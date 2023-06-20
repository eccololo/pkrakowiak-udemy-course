# [IN]: divisible_by_3_or_5(10, 30)
# [OUT]: [10, 12, 15, 18, 20, 21, 24, 25, 27, 30]
#
# [IN]: divisible_by_3_or_5(2, 14)
# [OUT]: [3, 5, 6, 9, 10, 12]


def divisible_by_3_or_5(start, stop):
    return [number for number in range(start, stop + 1) if number % 5 == 0 or number % 3 == 0]
