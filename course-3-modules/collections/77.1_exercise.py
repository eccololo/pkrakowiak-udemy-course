from collections import deque


daynames = deque(['Mon.', 'Tue.', 'Wed.', 'Thu.', 'Fri.', 'Sat.', 'Sun.'])

daynames.rotate(-3)
lastday = daynames.pop()
print(lastday)