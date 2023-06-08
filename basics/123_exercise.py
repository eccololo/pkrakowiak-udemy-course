# Załóżmy, że pracujesz nad projektem e-commerce i musisz utworzyć klasę o nazwie Product reprezentującą produkt w asortymencie sklepu internetowego. Klasa powinna mieć następujące atrybuty (atrybuty instancji):
#
# name: ciąg reprezentujący nazwę produktu
#
# price: liczba zmiennoprzecinkowa reprezentująca cenę produktu
#
# quantity: liczba całkowita reprezentująca ilość produktu w magazynie
#
#
#
# Wykorzystaj w implementacji metodę specjalną __init__() do ustawienia wymaganych atrybutów.
#
#
#
# Uwaga! W celu zaliczenia ćwiczenia należy tylko zaimplementować klasę. Nie trzeba niczego drukować do konsoli. Testy jednostkowe sprawdzają poprawność implementacji rozwiązania.

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity