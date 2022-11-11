import random
import string


def generate_password(length):
    password = ''.join(random.choice(string.printable) for i in range(length))
    return password
