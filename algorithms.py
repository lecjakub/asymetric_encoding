import enum
from rsa import Rsa
from ecb import Ecb

_ctors = {
    Algorythms.RSA.value : Rsa,
    Algorythms.ECB.value : Ecb}

class Algorythms(enum.Enum):
    RSA=0,
    ECB=1,
    def ctor(self):
        return _ctors[self.value]
