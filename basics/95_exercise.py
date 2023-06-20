# [IN]: count_kwargs(a=1, b=3)
# [OUT]: 2
#
# [IN]: count_kwargs(10, 'John', age=20, country='USA')
# [OUT]: 2
#
# [IN]: count_kwargs(30, 1)
# [OUT]: 0
#
# [IN]: count_kwargs()
# [OUT]: 0

def count_kwargs(**kwargs):
    return len(kwargs)