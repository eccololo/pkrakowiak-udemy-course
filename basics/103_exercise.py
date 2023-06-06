# Podana jest poniższa lista:
#
#
#
# words = ['cat', 'dog', 'rabbit', 'hamster', 'parrot', 'raccoon']
#
#
# Wykorzystaj list comprehension, aby utworzyć nową listę o nazwie r_words, która zawiera tylko słowa z oryginalnej listy słów words, które zaczynają się na literę 'r'. W odpowiedzi wynik wydrukuj do konsoli.
#
#
#
# Oczekiwany wynik:
#
#
#
# # ['rabbit', 'raccoon'

words = ['cat', 'dog', 'rabbit', 'hamster', 'parrot', 'raccoon']

print([word for word in words if word.startswith("r")])