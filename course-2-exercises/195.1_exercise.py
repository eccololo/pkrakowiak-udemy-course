numbers = [1, 2, 3, 4, 5]
user_input = 10
try:
    print(numbers[user_input]) # Modify this code
except IndexError:
    print('Index is out of range of the list.')
except:
    print('An unknown error occurred.')