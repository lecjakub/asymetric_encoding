from encrypting.logic.symkey import SymKey
from Crypto import Random
from Crypto.Cipher import AES
class Ecb():
        def __init__(self, sym_key):
            self.key = sym_key.key
            self.cipher = AES.new(self.key,AES.MODE_ECB)
        
        def encode(self, data):
            return self.cipher.encrypt(data)

        def decode(self, data):
            return self.cipher.decrypt(data)
        
        @staticmethod
        def generate_key(key_size):
            if not (key_size % 16 == 0):
                raise ArithmeticError("key size must be multiple of 16")
            rand =Random.new()
            return SymKey(rand.read(key_size))
        