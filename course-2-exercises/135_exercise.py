age = 22
ticket_type = 'economy'

if age < 18:
    print('Sorry, passengers under 18 years old.')
elif age >= 18 and ticket_type == "business":
    print('Passenger is eligible to board with a business ticket.')
elif age >= 65 and ticket_type == "economy":
    print("Passenger is eligible to board with an economy ticket.")
else:
    print('Sorry, passenger is not eligible to board the flight.')