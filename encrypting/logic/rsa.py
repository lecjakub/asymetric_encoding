
import sympy as sy
import random
import math
from encrypting.logic.asymkey import AsymKey

class Rsa():
    def __init__(self,key):
        if isinstance(key,AsymKey):
            self.private_key = key.private_key
            self.public_key = key.public_key
            self.key_bits = key.key_size
        else:
            self.key_bits = key
            self.init_keys()

    def encode(self, byte_stream):
        n, e, key_size = self.public_key
        result = bytearray()
        resolution = key_size * 2 // 8
        for i in byte_stream:
            x = pow(i, e, n)
            result.extend(x.to_bytes(resolution, 'little'))
        return result

    def decode(self, byte_stream):
        n, d, key_size = self.private_key
        result = bytearray()
        resolution = key_size * 2 // 8
        for i in range(0, len(byte_stream), resolution):
            byte = ( int.from_bytes(byte_stream[i:i+resolution], 'little'))
            x = pow(byte, d, n)
            if x > 255:
                return (0,1)
            result.extend(x.to_bytes(1,'little'))
        return (result, 0)

    def init_keys(self):
        p, q = self._gen_p_q(self.key_bits)
        n = p * q
        phi = (p-1) * (q-1)
        while True:
            e = random.randrange(2**(self.key_bits - 1), 2**self.key_bits)
            if math.gcd(e, phi) == 1:
                break
        d = self._mod_inverse(e, phi)
        self.public_key = (n, e, self.key_bits)
        self.private_key = (n, d, self.key_bits)

    @staticmethod
    def generate_key(key_bits):
        p, q = Rsa._gen_p_q(key_bits)
        n = p * q
        phi = (p-1) * (q-1)
        while True:
            e = random.randrange(2**(key_bits - 1), 2**key_bits)
            if math.gcd(e, phi) == 1:
                break
        d = Rsa._mod_inverse(e, phi)
        public_key = (n, e, key_bits)
        private_key = (n, d, key_bits)
        return AsymKey(key_bits,private_key,public_key)

    def set_public_key(self,pub_key):
        self.public_key = pub_key

    def set_private_key(self,priv_key):
        self.private_key = priv_key

    def _lcm(self, a: int, b: int):
        return int(a * b) // int(math.gcd(a, b))

    @staticmethod
    def _mod_inverse( a, m):               
        if math.gcd(a, m) != 1:
            return None
        u1, u2, u3 = 1, 0, a
        v1, v2, v3 = 0, 1, m
        while v3 != 0:
            q = u3 // v3
            v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
        return u1 % m

    @staticmethod
    def _gen_p_q( key_bits):
        random_prime = lambda: sy.randprime(2**(key_bits - 1), 2**key_bits)
        p = random_prime()
        q = random_prime()
        while q == p:
            q = random_prime()
        return p, q
