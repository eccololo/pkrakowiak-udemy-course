# [IN]: person_info(name='John', age=35, city='Los Angeles')
# [OUT]: 'John is 35 years old and lives in Los Angeles.'
#
# [IN]: person_info(name='Paul')
# [OUT]: Paul is <unknown> years old and lives in <unknown>.
#
# [IN]: person_info(name='Paul', city='Warsaw')
# [OUT]: Paul is <unknown> years old and lives in Warsaw.
#
# [IN]: person_info(age=30, city='New York')
# [OUT]: John is 30 years old and lives in New York.

def person_info(**kwargs):
    name = kwargs.get("name", default="<unknown>")
    age = kwargs.get("age", default="<unknown>")
    city = kwargs.get("city", default="<unknown>")
    return f'{name} is {age} years old and lives in {city}.'


person_info(name='Paul')
# [OUT]: Paul is <unknown> years old and lives in <unknown>.
