seat_assignment = 'Seat 24A'
boarding_group = 'Group C'
delay_time = '30 mins'
baggage_weight ='23 kg'

# Enter your solution here

clean_seat_assignment = seat_assignment.replace("Seat ", "")
clean_boarding_group = boarding_group.replace("Group ", "")
clean_delay_time = delay_time.replace(" mins", "")
clean_baggage_weight = baggage_weight.replace(" kg", "")

print(clean_seat_assignment)
print(clean_boarding_group)
print(clean_delay_time)
print(clean_baggage_weight)