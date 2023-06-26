# Wygeneruj wszystkie liczby parzyste od 2 do 18 włącznie.
# Następnie zapisz każdą liczbę w osobnej linii do pliku num.txt

even_list = [str(x) for x in range(2, 20) if x % 2 == 0]
with open("num.txt", "w") as f:
    for num in even_list:
        f.write(num + "\n")