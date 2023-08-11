weapon_type = 'sword'
armor_type = 'leather'

# Enter your solution here
dmg = None

if weapon_type == "sword":
    if armor_type == "leather":
        dmg = 10
    if armor_type == "chainmail":
        dmg = 5

if weapon_type == "axe":
    if armor_type == "leather":
        dmg = 5
    if armor_type == "chainmail":
        dmg = 10

if weapon_type == "bow":
    dmg = 5

print(f"The player can inflict {dmg} points of damage.")