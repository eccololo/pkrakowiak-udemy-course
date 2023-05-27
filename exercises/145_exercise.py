# Podana jest poniższa lista:
#
#
#
# items = ['P-1', 'R-2', 'D-4', 'F-6']
#
#
# Wykorzystując funkcję map() oraz wyrażenie lambda przekształć
# podaną listę w taki sposób, aby pozbyć się z każdego elementu
# znaku '-' (myślnik). Wynik wydrukuj do konsoli.

items = ['P-1', 'R-2', 'D-4', 'F-6']

print(list(map(lambda x: x.replace("-", ""), items)))
