import enum
from rsa import Rsa
from ecb import Ecb

class Algorithms(enum.Enum):
    RSA = 0
    ECB = 1

    def create(self,key):
        __ctors =  {
        self.RSA : Rsa,
        self.ECB : Ecb}
        
        c = __ctors[self]
        return c(key)
