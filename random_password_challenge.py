import random
import string

def generate_password(length):
    if length < 6:
        raise ValueError("Password length should be at least 6 characters.")

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits

    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits)
    ]

    all_characters = lower + upper + digits
    password += random.choices(all_characters, k=length - 3)

    random.shuffle(password)

    return ''.join(password)

# Example usage
password_length = 12
password = generate_password(password_length)
print(f"Generated password: {password}")
