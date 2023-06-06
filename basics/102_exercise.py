# Używając list comprehension wydrukuj do konsoli listę liczb od 0 do 30 (bez 30) podzielnych przez 4.
#
#
#
# Uwaga: Zadanie można zrobić przy pomocy jednej linii kodu.
#
#
#
# Oczekiwany wynik:
#
#
#
# [0, 4, 8, 12, 16, 20, 24, 28]

print([number for number in range(0, 30) if number % 4 == 0])
