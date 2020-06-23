import random
import string


def secret_key_gen():
    letters = string.ascii_lowercase
    return ''.join([random.choice(letters) for i in range(6)])
