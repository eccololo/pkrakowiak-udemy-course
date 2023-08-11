years_of_service = 5
performance_rating = 8.5

# Enter your solution here
grade = None

if years_of_service < 1:
    grade = "Private"
elif years_of_service < 3 and performance_rating >= 7.0:
    grade = 'Corporal'
elif years_of_service < 3 and performance_rating < 7.0:
    grade = 'Private First Class'
elif years_of_service < 6 and performance_rating >= 7.0:
    grade = 'Sergeant'
elif years_of_service < 6 and performance_rating < 7.0:
    grade = 'Corporal'
elif years_of_service >= 7 and performance_rating >= 7.0:
    grade = 'Staff Sergeant'
else:
    grade = 'Sergeant'

print(f"The soldier's rank is {grade}.")