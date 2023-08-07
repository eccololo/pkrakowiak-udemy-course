quiz_score = 87

# Enter your solution here

rate = None
if quiz_score < 60:
    rate = "F"
elif 60 <= quiz_score <= 69:
    rate = "D"
elif 80 <= quiz_score <= 89:
    rate = "B"
else:
    rate = "A"


print(f"The student's grade is \"{rate}\".")