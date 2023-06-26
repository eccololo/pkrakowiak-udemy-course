# [IN]: ['cat', 'dog', 'rabbit', 'hamster', 'parrot', 'raccoon']
# [OUT]: ['rabbit', 'raccoon']

words = ['cat', 'dog', 'rabbit', 'hamster', 'parrot', 'raccoon']

print([word for word in words if word.startswith("r")])