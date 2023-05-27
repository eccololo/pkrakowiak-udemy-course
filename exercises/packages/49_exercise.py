from collections import Counter


poll_1 = {'yes': 140, 'no': 120, None: 12}
poll_2 = {'yes': 113, 'no': 132, None: 9}

cnt1 = Counter(poll_1)
cnt2 = Counter(poll_2)

result = cnt1 + cnt2

print(result)
