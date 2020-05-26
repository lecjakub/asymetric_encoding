from encrypting.logic.symkey import SymKey
import os
import Crypto
from Crypto import Random
from Crypto.Cipher import AES
class Ctr():
        def __init__(self, sym_key):
            self.key = sym_key.key

            if sym_key.counter == None:
                self.counter = os.urandom(16)
            else:
                self.counter = sym_key.counter
            self.cipher = AES.new(self.key,AES.MODE_CTR,counter = lambda : self.counter)
        
        def encode(self, data):
            return self.cipher.encrypt(data)

        def decode(self, data):
            return self.cipher.decrypt(data)
        
        @staticmethod
        def generate_key(key_size):
            if not (key_size % 16 == 0):
                raise ArithmeticError("key size must be multiple of 16")
            rand =Random.new()
            return SymKey(rand.read(key_size),counter=os.urandom(16))
        