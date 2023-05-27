from collections import Counter


text = 'python programming - introduction'

cnt1 = Counter(text)

print(sorted(cnt1.items(), reverse=True, key=lambda item: item[1])[:3])