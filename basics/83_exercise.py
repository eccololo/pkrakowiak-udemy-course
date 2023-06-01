# Przy pomocy odpowiedniej funkcji wbudowanej oraz pętli for wydrukuj poniższe wartości do konsoli.
#
#
#
# Oczekiwany wynik:
#
#
#
# 1 2 3 4 5 6 7 8 9
# 0 2 4 6 8
# 100 90 80 70 60 50 40 30 20 10
#
#
# Zwróć uwagę na białe znaki. Po każdej liczbie wstawiony został znak spacji.

output_1 = [f"{number }" for number in range(1, 10)]
output_2 = [f"{number }" for number in range(9) if number % 2 == 0]
output_3 = [f"{number }" for number in range(10, 101, 10)[::-1]]

print(" ".join(output_1))
print(" ".join(output_2))
print(" ".join(output_3))