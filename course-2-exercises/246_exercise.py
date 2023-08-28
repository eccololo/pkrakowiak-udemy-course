def pascal_triangle():
    # Enter your solution here
    row = [1]
    yield row
    while True:
        row = (
                [1]
                + [row[i] + row[i + 1] for i in range(len(row) - 1)]
                + [1]
        )
        yield row


triangle = pascal_triangle()

for i in range(10):
    print(next(triangle))