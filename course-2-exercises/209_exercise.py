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

# Enter your solution here
with open("209_patient_data.txt", "w") as f:
    f.write(f"First name: {first_name}\n")
    f.write(f"Last name: {last_name}\n")
    f.write(f"Weight: {weight} kg\n")
    f.write(f"Height: {height} m\n")
    f.write(f"Date of birth: {date_of_birth}\n")
    chronic_conditions = ",".join(chronic_conditions)
    f.write(f"Chronic conditions: {chronic_conditions}\n")
    hm = ",".join(medications['hypertension_medications'])
    f.write(f"Hypertension medications: {hm}\n")
    dm = ",".join(medications['diabetes_medications'])
    f.write(f"Diabetes medications: {dm}\n")