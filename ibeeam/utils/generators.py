import random
import string

from rest_framework_simplejwt.tokens import RefreshToken


def generate_password(length):
    password = ''.join(random.choice(string.printable) for i in range(length))
    return password


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
