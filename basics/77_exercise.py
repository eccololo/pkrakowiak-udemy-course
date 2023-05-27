# Podane są poniższe informacje medyczne pacjenta:
#
#
#
# first_name = 'Jan'
# last_name = 'Kowalski'
# weight = 75.5
# height = 1.85
# date_of_birth = '1990-01-01'
# chronic_conditions = ['hypertension', 'diabetes']
# medications = {
#     'hypertension_medications': ['enalapril', 'hydrochlorothiazide'],
#     'diabetes_medications': ['metformin'],
# }
#
#
# Za pomocą metody write() zapisz powyższe dane pacjenta do pliku o nazwie patient_data.txt tak jak pokazano poniżej:
#
#
#
# First name: Jan
# Last name: Kowalski
# Weight: 75.5 kg
# Height: 1.85 m
# Date of birth: 1990-01-01
# Chronic conditions: hypertension, diabetes
# Hypertension medications: enalapril, hydrochlorothiazide
# Diabetes medications: metformin

first_name = 'Jan'
last_name = 'Kowalski'
weight = 75.5
height = 1.85
date_of_birth = '1990-01-01'
chronic_conditions = ['hypertension', 'diabetes']
medications = {
    'hypertension_medications': ['enalapril', 'hydrochlorothiazide'],
    'diabetes_medications': ['metformin'],
}

with open("77_patient_data.txt", "w") as f:
    f.write(f"First name: {first_name}\n")
    f.write(f"Last name: {last_name}\n")
    f.write(f"Weight: {weight} kg\n")
    f.write(f"Height: {height} m\n")
    f.write(f"Date of birth: {date_of_birth}\n")
    f.write(f"Chronic conditions: {','.join(chronic_conditions)}\n")
    ht_meds = ",".join(medications['hypertension_medications'])
    db_meds = medications['diabetes_medications'][0]
    f.write(f"Hypertension medications: {ht_meds}\n")
    f.write(f"Diabetes medications: {db_meds}\n")


