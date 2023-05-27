# print(1 / 0)
# int("f")
# float("sd")

# try:
#     zmienna1 = 1 / 0
# except ZeroDivisionError:
#     print("Nie dzieli się przez zero.")
#
# try:
#     zmienna2 = 4 + "4"
# except TypeError:
#     print("Nie można dodawać tekstu do liczby.")
#
# try:
#     zmienna3 = int("sd")
# except ValueError:
#     print("Zły tekst.")
#
# while True:
#     try:
#         x = int(input("Podaj liczbę: "))
#         break
#     except ValueError:
#         print("Musisz podać liczbę.")
# try:
#     with open("text.txt") as file:
#         for line in file:
#             print(line)
# except FileNotFoundError:
#     print("Plik nie istnieje.")
#
# raise TypeError("Błąd.")

# raise ValueError("Blad wartosci.")


def divine(x, y):
    try:
        x = int(x)
        y = int(y)
        return x / y
    except ZeroDivisionError:
        print("Nie można dzielić przez zero.")
    except ValueError:
        print("Musisz wprowadzić liczbę.")


# divine(3, 0)
print(divine("1", "2"))
print(divine("t", "2"))