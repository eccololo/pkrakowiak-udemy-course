from collections import deque


daynames = deque(['Mon.', 'Tue.', 'Wed.', 'Thu.', 'Fri.', 'Sat.', 'Sun.'])
daynames.reverse()
firstday = daynames.popleft()
print(firstday)