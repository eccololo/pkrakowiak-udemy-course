blood_pressure_results = [
    {'patient_id': 1, 'systolic': 118, 'diastolic': 72},
    {'patient_id': 2, 'systolic': 130, 'diastolic': 90},
    {'patient_id': 3, 'systolic': 120, 'diastolic': 80},
    {'patient_id': 4, 'systolic': 110, 'diastolic': 70},
    {'patient_id': 5, 'systolic': 140, 'diastolic': 95},
]

# Enter your solution here
# Ciśnienie skurczowe powinno zawierać się w przedziale [90, 120], zaś rozkurczowe [60, 80]

output_list = [patient for patient in blood_pressure_results
               if (90 <= patient["systolic"] <= 120) and
               80 >= patient['diastolic'] >= 60]

for item in output_list:
    print(item)
