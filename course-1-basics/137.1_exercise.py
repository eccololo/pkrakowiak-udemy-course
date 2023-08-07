goals_scored = 8
bonus_points = 0
score = goals_scored * 10 + bonus_points

# Enter your solution here
if goals_scored >= 5:
    score += 5
if goals_scored >= 10:
    score += 10

print(f"Total score of the team is {score}.")