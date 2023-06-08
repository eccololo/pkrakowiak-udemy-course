def reverse_string(string):
    return string[::-1]

def capitalize_string(string):
    return string.capitalize()

def count_vowels(string):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count