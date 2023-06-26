# import datetime
#
#
# def log(message, dt=datetime.datetime.utcnow):
#     print(dt(), message)
#
#
# def logi(*args):
#     for command in args:
#         log(command)

import datetime
import time

print(datetime.datetime.utcnow())


def log(message, dt=datetime.datetime.utcnow):
    print(dt(), message)


def logi(*args):
    for command in args:
        log(command)
        time.sleep(1)


# log("Uruchomienie systemu.")

logi("Uruchomienie Systemu", "Logowanie", "Restart", "Wylogowanie")
