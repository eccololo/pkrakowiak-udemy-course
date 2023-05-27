# Napisz funkcję o nazwie factorial(), która obliczy wartość silni z danej liczby.

def factorial(n):
    """This function calculate factorial of given number."""
    output = 1
    for i in range(1, n + 1):
        output *= i

    return output


print(factorial(4))
