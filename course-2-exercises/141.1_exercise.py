xp = 750

# Enter your solution here

level = None

if xp < 100:
    level = 1
if xp < 499:
    level = 2
if xp < 999:
    level = 3
if xp >= 1000:
    level = 4

print(f"The player is at level {level}.")