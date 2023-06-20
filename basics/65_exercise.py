# [IN]:
# proportions = {
#     'flour': 500,
#     'salt': 4,
#     'sugar': 200,
#     'butter': 150
# }

# [OUT]:
# To prepare 3000 g of dough, you need:
# Flour - 1756.44 g
# Salt - 14.05 g
# Sugar - 702.58 g
# Butter - 526.93 g

proportions = {
    'flour': 500,
    'salt': 4,
    'sugar': 200,
    'butter': 150
}

# Enter your solution here

assumed_sum = 3000
total_one_portion = sum([v for (k, v) in proportions.items()])
flour_ratio = round(proportions["flour"] / total_one_portion, 10)
salt_ratio = round(proportions["salt"] / total_one_portion, 10)
sugar_ratio = round(proportions["sugar"] / total_one_portion, 10)
butter_ratio = round(proportions["butter"] / total_one_portion, 10)

ratios = [("Flour", flour_ratio), ("Salt", salt_ratio), ("Sugar", sugar_ratio), ("Butter", butter_ratio)]
output = []
for ratio in ratios:
    output.append((ratio[0], round(assumed_sum * ratio[1], 2)))

print("To prepare 3000 g of dough, you need:")
for out in output:
    print(f"{out[0]} - {out[1]} g")

# To prepare 3000 g of dough, you need:
# Flour - 2000 g
# Salt - 16 g
# Sugar - 800 g
# Butter - 600 g