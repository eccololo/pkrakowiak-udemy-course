from functools import reduce


def longest_word(x, y):
    # Enter your solution here
    if x > y:
        return x
    elif y > x:
        return y
    else:
        return y


words = ['Python', 'jest', 'popularnym', 'językiem', 'programowania']
result = reduce(longest_word, words)
print(result)
