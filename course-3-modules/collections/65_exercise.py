from collections import namedtuple

Student = namedtuple(typename="Student", field_names=["name", "age", "specialization"])

s1 = Student('Mike', 21, 'physics')
s2 = Student('Kate', 20, 'mathematics')
s3 = Student('Bob', 21, 'information technology')

students = [s1, s2, s3]

for student in students:
    print(f"{student.name:4} : {student.age}: {student.specialization}")