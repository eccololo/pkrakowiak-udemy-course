def add_example(x, y):
    """Zwraca sume dwoch liczb.
    >>> add(3, 4)
    7

    >>> add(2, 8)
    10
    """
    return x + y


def add(x, y):
    """Zwraca sume dwoch liczb.
    """
    return x + y


if __name__ == '__main__':
    import doctest

    doctest.testfile('test.txt')
