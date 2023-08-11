age_str = 'Pawel'

# Enter your solution here
try:
    number = int(age_str)
except ValueError:
    print('Unable to convert the string to an integer.')
else:
    print(f'Success! The number is: {number}')
finally:
    print('The program has finished executing.')