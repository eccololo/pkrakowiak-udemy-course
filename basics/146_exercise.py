def max_min_diff(numbers):
    """
    Calculates the difference between the maximum and minimum number
    in the given list.

    :param numbers: A list of numbers.
    :return: The difference between the maximum and minimum number
    in the list.
    :raises ValueError: If the list is empty.
    """
    # Enter your solution here
    assert len(numbers) != 0
    return max(numbers) - min(numbers)


# Enter your solution here

try:
    max_min_diff([])
except AssertionError as msg:
    print(msg)
