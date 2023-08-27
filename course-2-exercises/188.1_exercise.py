number = 25
guess = 10
epsilon = 0.01
iteration = 0

# Enter your solution here
while abs(guess ** 2 - number) >= epsilon:
    guess = guess - (guess ** 2 - number) / (2 * guess)
    iteration += 1
    print(f"Iteration {iteration}: Estimated square root value = {guess:.6f}")

print(f"Estimated square root of {number} is {guess:.10f}")