# Podane są dwie listy:
#
#
#
# num1 = [4, 2, 6, 2, 11]
# num2 = [5, 2, 3, 3, 9]
#
#
# Listy są tej samej długości. Wykorzystując funkcję map()
# oraz wyrażenie lambda przekształć podane listy w jedną
# zawierającą resztę z dzielenia elementu pierwszej listy
# przez odpowiedni element drugiej listy.

num1 = [4, 2, 6, 2, 11]
num2 = [5, 2, 3, 3, 9]
output_list = list(map(lambda x: x[0] % x[1], list(zip(num1, num2))))
print(output_list)
