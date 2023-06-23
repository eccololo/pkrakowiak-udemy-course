# Zaimplementuj klasę Developer ktora zwroci True jesli programista programuje w Python. Jesli nie to False.

class Developer:

    def __init__(self, name, age, programming_language):
        self.name = name
        self.age = age
        self.programming_language = programming_language

    @staticmethod
    def is_python_programmer(programmer):
        return programmer.lower() == "python"
