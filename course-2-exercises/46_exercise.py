text = 'Programming in python.'
vowels = {'a', 'e', 'i', 'o', 'u'}
text = text.lower()
text = text.replace(" ", "").replace(".", "")
text = set(text)
text = text.difference(vowels)
print(text)