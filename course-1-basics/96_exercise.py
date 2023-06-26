# [IN]: create_dictionary(age=20, name='Mike')
# [OUT]: {'age': 20, 'name': 'Mike'}
#
# [IN]: create_dictionary(level='senior', stack=['python', 'aws', 'sql'])
# [OUT]: {'level': 'senior', 'stack': ['python', 'aws', 'sql']}
#
# [IN]: create_dictionary(country='Poland')
# [OUT]: {'country': 'Poland'}

def create_dictionary(**kwargs):
    return {key: value for (key, value) in kwargs.items()}
