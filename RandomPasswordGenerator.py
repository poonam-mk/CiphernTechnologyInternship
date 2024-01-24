import random
import string

def generate_password(length=8):

    # Define the character sets for the password
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine all character sets
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Ensure the password length is at least 8 characters
    length = max(length, 8)

    # Generate a random password using random.choices
    password = ''.join(random.choices(all_characters, k=length))

    return password


password = generate_password()
print("Generated Password:", password)