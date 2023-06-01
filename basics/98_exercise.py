# Załóżmy, że podany jest poniższy słownik określający pewną konfigurację środowiska pracy:
#
#
#
# config = {'env': 'development', 'team': 'data science'}
#
#
# Zaimplementuj funkcję o nazwie update_config(), która będzie zmieniać wartość globalnej zmiennej config na podstawie przekazanych do niej argumentów typu klucz-wartość. Zmienna config powinna być zdefiniowana poza funkcją.
#
#
#
# Następnie wywołaj zaimplementowaną funkcję tak jak poniżej:
#
#
#
# update_config(env='testing')
#
#
# W odpowiedzi wydrukuj słownik config do konsoli.
#
#
#
# Oczekiwany wynik:
#
#
#
# {'env': 'testing', 'team': 'data science'}

config = {'env': 'development', 'team': 'data science'}


def update_config(**kwargs):
    global config
    for key, value in kwargs.items():
        config[key] = value


update_config(env='testing')
print(config)