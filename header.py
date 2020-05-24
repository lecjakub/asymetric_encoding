from abc import ABC,abstractmethod
import numpy as np
from struct import unpack

class Header(ABC):
    def __init__(self,file):
        self.size = unpack('I',file.read(4)) #reading unsigned int containing size of header
        self.final = unpack('?',file.read(1))
        if not self.final:
            self.next_alg = 
