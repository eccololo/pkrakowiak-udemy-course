from collections import Counter


poll_1 = {'yes': 140, 'no': 120, None: 12}
poll_2 = {'yes': 113, 'no': 132, None: 9}
poll_3 = {'yes': 16, 'no': 14}

cnt1 = Counter(poll_1)
cnt2 = Counter(poll_2)
cnt3 = Counter(poll_3)

result = cnt1 + cnt2 + cnt3

print(result["yes"])