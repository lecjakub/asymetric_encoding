import enum
from rsa import Rsa
from ecb import Ecb
from cbc import Cbc
from ctr import Ctr


class Algorithms(enum.Enum):
    RSA = 0
    ECB = 1
    CBC = 2
    CTR = 3

    def create(self,key):
        __ctors =  {
        self.RSA : Rsa,
        self.ECB : Ecb,
        self.CBC : Cbc,
        self.CTR : Ctr}

        c = __ctors[self]
        return c(key)


