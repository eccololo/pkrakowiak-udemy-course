# [IN]: sort_by_length(['apple', 'pear', 'banana', 'pineapple', 'orange'])
# [OUT]: ['pear', 'apple', 'banana', 'orange', 'pineapple']
#
# [IN]: sort_by_length(['laptop', 'mouse', 'keyboard', 'screen'])
# [OUT]: ['mouse', 'laptop', 'screen', 'keyboard']

def sort_by_length(words_list):
    return sorted(words_list, key=lambda x: len(x))
