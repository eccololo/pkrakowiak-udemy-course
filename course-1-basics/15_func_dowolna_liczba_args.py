def tests_args(x, *args):
    print("Pierwszy parametr", x)
    for arg in args:
        print("Kolejny parametr *args", arg)


tests_args(1, 2, 3, 4, 5, 6, 7)


def funkcja_1(x, y, *args):
    print("x=", x)
    print("y=", y)
    print("*args=", args)


funkcja_1(1, 2)
funkcja_1(1, 2, 3, 4, 5)


def suma(x, y):
    return x + y


print(suma(1, 2))


def suma_dowol(*args):
    return sum(args)


print(suma_dowol(1, 2, 3, 4, 5, 6, 7))


def funkcja_2(**kwargs):
    for kwarg in kwargs:
        print("Nastepny argument kwarg:", kwarg)


funkcja_2(**{"a": 1, "b": 2})


def funkcja_3(**kwargs):
    print(kwargs)


print(funkcja_3(a=1, b=4))


def funkcja_4(*args, **kwargs):
    print(args)
    print(kwargs)


funkcja_4(1, 2, 3, 4, a=1, b=2)