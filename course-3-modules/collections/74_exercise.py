from collections import deque

days = ['Tue.', 'Wed.', 'Thu.', 'Fri.', 'Sat.']
daynames = deque(days)
daynames.append("Sun.")
daynames.appendleft("Mon.")
print(daynames)