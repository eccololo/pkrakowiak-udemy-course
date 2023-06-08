def encrypt(message, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encrypted_message = ""
    for char in message:
        if char.lower() in alphabet:
            char_index = alphabet.index(char.lower())
            encrypted_char = key[char_index]
            if char.isupper():
                encrypted_char = encrypted_char.upper()
            encrypted_message += encrypted_char
        else:
            encrypted_message += char
    return encrypted_message

def decrypt(message, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    decrypted_message = ""
    for char in message:
        if char.lower() in alphabet:
            char_index = key.index(char.lower())
            decrypted_char = alphabet[char_index]
            if char.isupper():
                decrypted_char = decrypted_char.upper()
            decrypted_message += decrypted_char
        else:
            decrypted_message += char
    return decrypted_message
