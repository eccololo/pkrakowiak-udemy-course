hotel_booking = {'hotel_name': 'Sheraton',
                 'check_in_date': '2024-06-10',
                 'check_out_date': '2023-06-13',
                 'room_type': 'Deluxe',
                 'num_guests': 2}

hotel_booking["num_guests"] = 3
hotel_booking["price"] = 200
del hotel_booking['room_type']
print(len(hotel_booking))
print(sorted(hotel_booking.keys()))