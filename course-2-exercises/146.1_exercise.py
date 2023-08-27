score = 7000
lives = 2

# Enter your solution here

level = None
if score < 1000:
    level = 1
elif 4999 > score > 1000:
    level = 2
elif 9999 > score > 5000:
    if lives >= 1:
        level = 3
    else:
        level = 2
elif score >= 10000:
    if lives >= 2:
        level = 4
    elif lives == 1:
        level = 3
    else:
        level = 2

print(f"The player is at level {level}.")

