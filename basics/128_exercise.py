# Zaimplementuj klasę Developer, która ma trzy zmienne instancji: name, age i programming_language, które są inicjowane w metodzie konstruktora __init__(). Zaimplementuj również metodę statyczną is_python_programmer(), która pobiera język programowania i zwraca True, jeśli jest to Python, lub False w przeciwnym razie (rozwiązanie ma być niewrażliwe na wielkość liter). Pamiętaj, że metoda ta ma być metodą statyczną.
#
#
#
# Uwaga! W celu zaliczenia ćwiczenia należy tylko zaimplementować klasę. Nie trzeba niczego drukować do konsoli. Testy jednostkowe sprawdzają poprawność implementacji rozwiązania.

class Developer:

    def __init__(self, name, age, programming_language):
        self.name = name
        self.age = age
        self.programming_language = programming_language

    @staticmethod
    def is_python_programmer(programmer):
        return programmer.lower() == "python"
