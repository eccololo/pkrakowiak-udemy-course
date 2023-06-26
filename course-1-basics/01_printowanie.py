print("Pyth" "On")

# Przelamanie dlugiego ciagu znakow tak aby byl lepiej widoczny w IDE.
url = ("https://www.abs.com/aaaaaaaaaaaaaaaaaaaavvvvvvvvvvvvvvvvv"
       "sssssssssssssssssssssssssssseeeeeeeeeeeeeeeeeee/29")

print(url)


# Sposob printowania int bez wczesniejszej konwersji za pomoca funkcji print.
imie = "Mateusz"
age = 35

print(imie, age)
print("{} ma {} lat".format(imie, age))
print("{1} ma {0} lat".format(imie, age))