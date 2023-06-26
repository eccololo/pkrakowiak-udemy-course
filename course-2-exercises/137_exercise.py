# Zdefiniuj funkcję is_palindrome(), która za argument przyjmie
# obiekt typu str i sprawdzi czy podany string jest palindromem
# (wyrażenie brzmiące tak samo czytane od lewej do prawej i od prawej do lewej).
#
# Jeżeli tak, funkcja ma zwracać wartość logiczną True, przeciwnie False.

def is_palindrome(word):
    return word == word[::-1]


print(is_palindrome("kajak"))
