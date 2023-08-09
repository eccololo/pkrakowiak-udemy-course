def area(w, h):
    if not (isinstance(w, (int, float)) and isinstance(h, (int, float))):
        raise TypeError("Width and height must be value of type int or float.")

    if not (w > 0 and h > 0):
        raise ValueError("Width and height must be value greater than 0.")

    return w * h