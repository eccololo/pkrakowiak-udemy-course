from collections import deque


daynames = deque(['Mon.', 'Tue.', 'Wed.', 'Thu.', 'Fri.', 'Sat.', 'Sun.'])
daynames.reverse()
first_item = daynames.popleft()
print(first_item)