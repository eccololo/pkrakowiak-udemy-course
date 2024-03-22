from collections import ChainMap

default_settings = {"mode": "eco", "power_level": 7}
user_settings = {"mode": None, "power_level": None}

settings = ChainMap( default_settings, user_settings)

print(settings["mode"])