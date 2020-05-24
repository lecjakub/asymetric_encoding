from algorithm import Algorithm
from Crypto.Cipher import AES
class Ecb(Algorithm):
        def __init__(self, key):
            self.key = key
            self.cipher = AES.new(self.key,AES.MODE_ECB)
        
        def encode(self, data):
            return self.cipher.encrypt(data), self.key

        def decode(self, data):
            return self.cipher.decrypt(data)