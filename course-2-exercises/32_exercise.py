num_of_cars = 200
num_of_parts = 1500
cost_per_part = 20
profit_per_car = 500

# Enter your solution here
total_cost = num_of_cars * num_of_parts * cost_per_part
total_profit = num_of_cars * profit_per_car
total_revenue = total_profit + total_cost
profit_margin = (total_revenue - total_cost) / total_revenue

print(f"Total revenue: {total_revenue}")
print(f"Profit margin: {profit_margin:.4f}")