# [IN]: Plik 72_data.txt

# [OUT]:
# 2023-03-31 12:00:00,2.3
# 2023-03-31 12:01:00,3.1
# 2023-03-31 12:02:00,2.7
# Total power generated: 8.10 MW

with open("72_data.txt", "r") as f:
    suma = 0
    for line in f:
        line = line.replace("\n", "")
        print(line)
        suma += float(line.split(",")[1])

print(f"Total power generated: {round(suma, 2)}0 MW")