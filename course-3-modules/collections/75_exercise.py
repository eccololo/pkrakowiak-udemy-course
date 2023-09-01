from collections import deque


daynames = deque(['Mon.', 'Tue.', 'Wed.', 'Thu.', 'Fri.', 'Sat.', 'Sun.'])
daynames.rotate(1)
print(daynames)