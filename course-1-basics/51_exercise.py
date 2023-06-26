height = 1.9
weight = 104

# Enter your solution here
bmi = round(weight / (height ** 2), 2)
if bmi < 18.5:
    print('Underweight')
elif bmi >= 18.5 and bmi < 25:
    print('Normal weight')
elif bmi >= 25 and bmi < 30:
    print('Overweight')
elif bmi >= 30:
    print('Obese')
