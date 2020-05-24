from algorithm import Algorithm
import sympy as sy
import random
import math

class Rsa():
    def __init__(self,key_bits, private_key=None, public_key=None):
        #super.__init__(key)
        if key_bits is None and private_key is None and public_key is None:
            pass
            #raise NotImplementedError
        self.private_key = private_key
        self.public_key = public_key
        self.key_bits = key_bits

    def encode(self, byte_stream):
        n, e, key_size = self.public_key
        result = bytearray()
        resolution = key_size * 2 // 8
        for i in byte_stream:
            x = pow(i, e, n)
            result.extend(x.to_bytes(resolution, 'little'))
        return (result, 0)

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

    def generate_keys(self):
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

    def load_private_key(self):
        pass

    def load_public_key(self):
        pass

    def load_key(self):
        pass

    def set_public_key(self,pub_key):
        self.public_key = pub_key

    def set_private_key(self,priv_key):
        self.private_key = priv_key

    def _lcm(self, a: int, b: int):
        return int(a * b) // int(math.gcd(a, b))

    def _mod_inverse(self, a, m):               
        if math.gcd(a, m) != 1:
            return None
        u1, u2, u3 = 1, 0, a
        v1, v2, v3 = 0, 1, m
        while v3 != 0:
            q = u3 // v3
            v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
        return u1 % m

    def _gen_p_q(self, key_bits):
        random_prime = lambda: sy.randprime(2**(key_bits - 1), 2**key_bits)
        p = random_prime()
        q = random_prime()
        while q == p:
            q = random_prime()
        return p, q

    

    # def encrypt_file(input_file , output_file, publicKey):
    #     with open(input_file, "rb") as text_file:
    #         bytes_stream = text_file.read()
    #         encoded = algorithms.encrypt_rsa(bytes_stream, publicKey)

    #         with open(output_file, 'wb+') as encoded_file:
    #             encoded_file.write(encoded)


    # def decrypt_file(input_file : str, output_file: str, privateKey):
    #     with open(input_file,"rb") as encoded_file:
    #         encoded = encoded_file.read()
    #         decoded = algorithms.decrypt_rsa(encoded, privateKey)
    #         with open(output_file,'wb+') as decoded_file:
    #             decoded_file.write(decoded)
    
    # def encrypt_file(bytes_stream, key):
    #     n, e, key_size = key
    #     result = []
    #     for byte in bytes_stream:
    #         x = pow(byte, e, n)
    #         y = x.to_bytes(key_size* 2 // 8, 'little')
    #         result.extend(y)
    #     return bytearray(result)

    # def decrypt_file(bytes_stream, key):
    #     n, d, key_size = key
    #     resolution = key_size * 2 // 8
    #     decoded_bytes = []
    #     for i in range(0, len(bytes_stream), resolution):
    #         byte = ( int.from_bytes(bytes_stream[i:i + resolution], 'little'))
    #         x = pow(byte, d, n)
    #         decoded_bytes.extend(x.to_bytes(1,'little'))
    #     return bytearray(decoded_bytes)