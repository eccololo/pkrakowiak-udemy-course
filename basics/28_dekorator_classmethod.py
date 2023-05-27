class Student:

    lista_studentow = []

    def __init__(self, imie, nazwisko, wiek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
        self.lista_studentow.append(self)
    
    @classmethod
    def get_dlugosc_listy_stodentow(cls):
        print(len(Student.lista_studentow))


student_1 = Student("Jan", "Kowalski", 25)
student_2 = Student("Tomasz", "Kowal", 23)
student_3 = Student("Ola", "Hyla", 24)

Student.get_dlugosc_listy_stodentow()