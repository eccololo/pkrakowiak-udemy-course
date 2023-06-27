seat_assignment = ' 24A '
gate_announcement = 'Boarding for flight UA 123 has begun.'
seat_assignment = '24a'
gate_number = 'B12'
cities = ['New York', 'Los Angeles', 'Chicago']

# Enter your solution here
clean_seat_assignment = seat_assignment.strip()
updated_announcement = gate_announcement.replace("Departing", "Boarding")
uppercase_seat = seat_assignment.upper()
gate = gate_number[1:]
terminal = gate_number[:1]
cities_string = ",".join(cities)

print(clean_seat_assignment)
print(updated_announcement)
print(uppercase_seat)
print(terminal)
print(gate)
print(cities_string)