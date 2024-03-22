from collections import Counter

poll_1 = {'yes': 140, 'no': 120, None: 12}
poll_2 = {'yes': 113, 'no': 132, None: 9}
poll_3 = {'yes': 16, 'no': 14}

output_1 = Counter(poll_1)
output_2 = Counter(poll_2)
output_3 = Counter(poll_3)

output = output_1 + output_2 + output_3

print(output['yes'])