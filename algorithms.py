import math
import random
import sympy as sy


def lcm(a: int, b: int):
    return int(a * b) // int(math.gcd(a, b))


def _mod_inverse(a, m):
    x = 1
    while x < m:
        if (a * x) % m == 1:
            return x
        x += 1
    return 1

def mod_inverse(a, m):                 # nie kłamie  #pani to je uczciwy człowiek #######  NASZE !!!!!!!!!!!!!!!!!!!!! NIEKRADZIONE !!!!!!!!!!!!!!!!!!!!!!!!!
    if math.gcd(a, m) != 1:
       return None
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
   
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m


def gen_p_q(key_bits):
    random_prime = lambda: sy.randprime(2**(key_bits - 1), 2**key_bits)
    p = random_prime()
    q = random_prime()
    while q == p:
        q = random_prime()
    return p, q

def get_keys(key_bits):
    p, q = gen_p_q(key_bits)
    n = p * q
    phi = (p-1) * (q-1)

    while True:
        e = random.randrange(2**(key_bits - 1), 2**key_bits)
        if math.gcd(e, phi) == 1:
                break

    d = mod_inverse(e, phi)

    public_key = (n, e, key_bits)
    private_key = (n, d, key_bits)

    return public_key, private_key


def encrypt_rsa(bytes_stream, key):
    n, e, key_size = key
    result = []
    for byte in bytes_stream:
        x = pow(byte, e, n)
        #x = (byte ** e) % n
        y = x.to_bytes(key_size* 2 // 8, 'little')
        result.extend(y)
    return bytearray(result)
    # return 'zakodowana dupa'
      

def decrypt_rsa(bytes_stream, key):
    n, d, key_size = key
    resolution = key_size * 2 // 8

    decoded_bytes = []
    for i in range(0, len(bytes_stream), resolution):
        byte = ( int.from_bytes(bytes_stream[i:i + resolution], 'little'))
        x = pow(byte, d, n)
        decoded_bytes.extend(x.to_bytes(1,'little'))

    return bytearray(decoded_bytes)
