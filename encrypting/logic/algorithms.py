import enum
from encrypting.logic.rsa import Rsa
from encrypting.logic.ecb import Ecb
from encrypting.logic.cbc import Cbc
from encrypting.logic.ctr import Ctr

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

