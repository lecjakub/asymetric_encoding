import enum
from encrypting.logic.rsa import Rsa
from encrypting.logic.ecb import Ecb
from encrypting.logic.cbc import Cbc
from encrypting.logic.ctr import Ctr

def generate_asymmetric_key(algorithm:str):
    keys = {
        'rsa1024': lambda: Rsa.generate_key(1024),
        'rsa2048': lambda: Rsa.generate_key(2048)
    }
    return keys[algorithm]()

class Algorithms(enum.Enum):
    RSA = 0
    ECB = 1
    CBC = 2
    CTR = 3

    def create(self, key):
        __ctors = {
            self.RSA: Rsa,
            self.ECB: Ecb,
            self.CBC: Cbc,
            self.CTR: Ctr}

        c = __ctors[self]
        return c(key)

    @property
    def get_type(self):
        __ctors = {
            self.RSA: Rsa,
            self.ECB: Ecb,
            self.CBC: Cbc,
            self.CTR: Ctr}
        return __ctors[self]

