flights = {'AA100', 'UA200', 'DL300', 'WN400'}
booked_flights = {'AA100', 'WN400'}
available_flights = flights.difference(booked_flights)

print(available_flights)