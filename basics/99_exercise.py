# [IN]: fib = fibonacci()
# [IN]: next(fib)
# [OUT]: 0
# [IN]: next(fib)
# [OUT]: 1
# [IN]: next(fib)
# [OUT]: 1
# [IN]: next(fib)
# [OUT]: 2
# [IN]: next(fib)
# [OUT]: 3
# [IN]: next(fib)
# [OUT]: 5

def fibonacci():
    nth1 = 0
    nth2 = 1
    while True:
        yield nth1
        nth1, nth2 = nth2, nth1 + nth2


print(next(fibonacci()))
