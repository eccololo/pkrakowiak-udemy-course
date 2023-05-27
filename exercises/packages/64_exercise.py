from collections import namedtuple

Student = namedtuple(typename="Student", field_names=["name", "age", "specialization"])

mike = Student("Mike", 21, "physics")
kate = Student("Kate", 20, "mathematics")
bob = Student("Bob", 21, "information technology")

students = []
students.append(mike)
students.append(kate)
students.append(bob)

for student in students:
    print(f"{student.name:5} : {student.age}: student.specialization")
