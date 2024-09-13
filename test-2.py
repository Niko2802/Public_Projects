import random
import string

def generate_password(length=8):
    characters = string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


print(generate_password())