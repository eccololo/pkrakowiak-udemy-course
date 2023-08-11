num_nights = 10
discount_code = 'SUMMER20'

# Enter your solution here

cost_per_night = 100
total_cost = None
discount = None
if num_nights > 7 or discount_code == 'WINTER10':
    discount = 0.1
    total_cost = (num_nights * cost_per_night) * (1 - discount)
if discount_code == 'SUMMER20':
    discount = 0.2
    total_cost = (num_nights * cost_per_night) * (1 - discount)
if not discount_code:
    print('No discount will be applied.')

print(f"Total cost of the hotel room is $ {total_cost}.")