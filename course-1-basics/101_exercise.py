# [IN]: patients = patient_generator('patients.txt')
# [IN]: next(patients)
# [OUT]: 'name': 'John Smith', 'age': 30}
# [IN]: next(patients)
# [OUT]: {'name': 'Jane Doe', 'age': 45}
# [IN]: next(patients)
# [OUT]: {'name': 'Mike Johnson', 'age': 55}
# [IN]: next(patients)
# [OUT]: {'name': 'Emily Taylor', 'age': 22}
# [IN]: next(patients)
# [OUT]: StopIteration Error

# [OUT]:
# {'name': 'John Smith', 'age': 30}
# {'name': 'Jane Doe', 'age': 45}
# {'name': 'Mike Johnson', 'age': 55}
# {'name': 'Emily Taylor', 'age': 22}

def patient_generator(filename):
    with open(filename, "r") as f:
        data = f.readlines()
        for line in data:
            name = line.split(",")[0]
            age = int(line.split(",")[1].replace("\n", ""))
            yield {"name": name, "age": age}


for patient in patient_generator("101_patients.txt"):
    print(patient)
