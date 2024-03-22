from collections import Counter
from itertools import islice

text = 'python programming - introduction'

output = sorted(Counter(text).items(), key=lambda x: x[1], reverse=True)

print(output[:3])

