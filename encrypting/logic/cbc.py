from encrypting.logic.symkey import SymKey
from Crypto import Random
from Crypto.Cipher import AES
class Cbc():
        def __init__(self, sym_key):
            self.key = sym_key.key

            if sym_key.init_vector == None:
                self.iv = Random.new().read(AES.block_size)       
            else:
                self.iv = sym_key.init_vector
            
            self.cipher = AES.new(self.key,AES.MODE_CBC, self.iv)
     
        def encode(self, data):
            return self.cipher.encrypt(data)

        def decode(self, data):
            return self.cipher.decrypt(data)
        
        @staticmethod
        def generate_key(key_size):
            if not (key_size % 16 == 0):
                raise ArithmeticError("key size must be multiple of 16")
            rand = Random.new()
            return SymKey(rand.read(key_size),rand.read(AES.block_size))