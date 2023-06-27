seat_map_header = 'SEAT MAP'
row1 = ['A1', 'B1', 'C1', 'D1', 'E1', 'F1']
row2 = ['A2', 'B2', 'C2', 'D2', 'E2', 'F2']

# Enter your solution here
row_h1 = " - ".join(row1[:3])
row_h2 = " - ".join(row1[-3:])
row_h3 = " - ".join(row2[:3])
row_h4 = " - ".join(row2[-3:])
print(f"----------{seat_map_header}---------")
print(row_h1, "|", row_h2)
print(row_h3, "|", row_h4)
