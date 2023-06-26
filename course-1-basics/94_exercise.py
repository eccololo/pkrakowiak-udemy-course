# [IN]: join_strings('this', 'is', 'an', 'example')
# [OUT]: 'this is an example'
#
# [IN]: join_strings('Python', 'is', 'awesome')
# [OUT]: 'Python is awesome'
#
# [IN]: join_strings()
# [OUT]: ''


def join_strings(*args):
    return " ".join(args)