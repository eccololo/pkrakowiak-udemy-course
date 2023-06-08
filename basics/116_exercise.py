# Załóżmy, że budujesz narzędzie do szyfrowania i deszyfrowania wiadomości za pomocą prostego szyfru podstawieniowego i chcesz użyć modułu cipher.py do obsługi operacji szyfrowania i deszyfrowania.
#
#
#
# Zaimportuj odpowiednio funkcję decrypt() i używając klucza 'phqgiumeaylnofdxkrcvstzwb' (argument key funkcji encrpyt()) odszyfruj poniższą wiadomość:
#
# 'Mripv! Bds gag av!'
#
#
#
# Odszyfrowaną wiadomość wydrukuj do konsoli.

from cipher_115 import decrypt
key = 'phqgiumeaylnofdxkrcvstzwb'
print(decrypt('Mripv! Bds gag av!', key))