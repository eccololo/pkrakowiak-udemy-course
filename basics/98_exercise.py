# [IN]: {'env': 'development', 'team': 'data science'}
# [OUT]: {'env': 'testing', 'team': 'data science'}

config = {'env': 'development', 'team': 'data science'}


def update_config(**kwargs):
    global config
    for key, value in kwargs.items():
        config[key] = value


update_config(env='testing')
print(config)