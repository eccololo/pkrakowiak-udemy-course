# [OUT]: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

def print_odd_numbers():
    return [number for number in range(1, 20) if number % 2 != 0]


print(print_odd_numbers())
