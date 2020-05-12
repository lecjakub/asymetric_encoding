import math
import random


def lcm(a: int, b: int):
    return int(a*b / math.gcd(a, b))


def mod_inverse(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return 1


def get_keys(p, q):
    n = p * q
    phi = lcm(p - 1, q - 1)

    shuffle_array = list(range(2, phi))
    random.shuffle(shuffle_array)

    for e in shuffle_array:
        if math.gcd(e, phi) == 1:
            break

    d = mod_inverse(e, phi)

    public_key = (n, e)
    private_key = (n, d)

    return public_key, private_key


def encrypt_rsa(text, key):
    # n, k = key  
    # return [(((byte ** k) % n) % 256).to_bytes(1,'little') for byte in text]
    return 'zakodowana dupa'
    

def decrypt_rsa(text, key):
    # n, k = key
    # return [((byte ** k) % n) for byte in text]
    return  'odkodowana dupa'
