import random
import string


def generate_password(length=8):
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    length = max(length, 8)

    password = ''.join(random.choices(all_characters, k=length))

    return password


password = generate_password()
print("Generated Password:", password)
