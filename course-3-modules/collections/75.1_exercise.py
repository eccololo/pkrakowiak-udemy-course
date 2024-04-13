from collections import deque

daynames = deque()
daynames.append("Mon.")
daynames.append("Tue.")
daynames.append("Wed.")
daynames.append("Thu.")
daynames.append("Fri.")
daynames.append("Sat.")
daynames.append("Sun.")

print(daynames)

# Better solution

daynames = deque(["Tue.", "Wed.", "Thu.", "Fri.", "Sat."])
daynames.appendleft('Mon.')
daynames.append('Sun.')

print(daynames)