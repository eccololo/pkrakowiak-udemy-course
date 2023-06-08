# Załóżmy, że budujesz narzędzie do szyfrowania i deszyfrowania wiadomości za pomocą prostego szyfru podstawieniowego i chcesz użyć modułu cipher.py do obsługi operacji szyfrowania i deszyfrowania.
#
#
#
# Zaimportuj odpowiednio funkcję encrypt() i używając klucza 'phqgiumeaylnofdxkrcvstzwb' (argument key funkcji encrpyt()) zaszyfruj poniższą wiadomość:
#
# 'Python is cool'
#
#
#
# Zaszyfrowaną wiadomość wydrukuj do konsoli.
#
#
#
# Oczekiwany wynik:
#
#
#
# Xbvedf ac qddn

from cipher_115 import encrypt
key = 'phqgiumeaylnofdxkrcvstzwb'
print(encrypt('Python is cool', key))